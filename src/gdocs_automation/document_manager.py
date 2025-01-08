from typing import List, Dict, Any
import json

class DocumentManager:
    def __init__(self, automation):
        self.automation = automation
        self.current_doc = None
    
    def create_document(self, title: str) -> str:
        """Create a new Google Doc"""
        doc = self.automation.docs_service.documents().create(
            body={'title': title}
        ).execute()
        return doc.get('documentId')
    
    def insert_text(self, doc_id: str, text: str, index: int = 1) -> None:
        """Insert text at specified position"""
        requests = [{
            'insertText': {
                'location': {'index': index},
                'text': text
            }
        }]
        self.automation.docs_service.documents().batchUpdate(
            documentId=doc_id,
            body={'requests': requests}
        ).execute()
    
    def apply_formatting(self, doc_id: str, start_index: int, 
                        end_index: int, formatting: Dict[str, Any]) -> None:
        """Apply formatting to a range of text"""
        requests = [{
            'updateTextStyle': {
                'range': {
                    'startIndex': start_index,
                    'endIndex': end_index
                },
                'textStyle': formatting,
                'fields': ','.join(formatting.keys())
            }
        }]
        self.automation.docs_service.documents().batchUpdate(
            documentId=doc_id,
            body={'requests': requests}
        ).execute() 