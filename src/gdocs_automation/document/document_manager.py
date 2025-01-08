from typing import Dict, Any, Optional, List
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from ..core.error_handler import handle_errors, DocumentError
import logging

class DocumentManager:
    """Manages Google Docs operations"""
    
    def __init__(self, credentials: Credentials):
        self.service = build('docs', 'v1', credentials=credentials)
        self.drive_service = build('drive', 'v3', credentials=credentials)
        self.logger = logging.getLogger(__name__)

    @handle_errors(error_types=(Exception,))
    def create_document(self, title: str) -> str:
        """Create a new Google Doc"""
        try:
            doc = self.service.documents().create(body={'title': title}).execute()
            self.logger.info(f"Created document: {title}")
            return doc.get('documentId')
        except Exception as e:
            raise DocumentError(f"Failed to create document: {str(e)}")

    @handle_errors(error_types=(Exception,))
    def get_document(self, document_id: str) -> Dict[str, Any]:
        """Get document content"""
        return self.service.documents().get(documentId=document_id).execute()

    @handle_errors(error_types=(Exception,))
    def update_document(self, document_id: str, requests: List[Dict[str, Any]]) -> None:
        """Update document with batch requests"""
        self.service.documents().batchUpdate(
            documentId=document_id,
            body={'requests': requests}
        ).execute()

    @handle_errors(error_types=(Exception,))
    def insert_text(self, document_id: str, text: str, index: int = 1) -> None:
        """Insert text at specified position"""
        requests = [{
            'insertText': {
                'location': {'index': index},
                'text': text
            }
        }]
        self.update_document(document_id, requests)

    @handle_errors(error_types=(Exception,))
    def apply_style(self, document_id: str, start_index: int, 
                   end_index: int, style: Dict[str, Any]) -> None:
        """Apply text style to a range"""
        requests = [{
            'updateTextStyle': {
                'range': {
                    'startIndex': start_index,
                    'endIndex': end_index
                },
                'textStyle': style,
                'fields': ','.join(style.keys())
            }
        }]
        self.update_document(document_id, requests) 