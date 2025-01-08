from gdocs_automation.core import GoogleDocsAutomation
from gdocs_automation.document_manager import DocumentManager
from gdocs_automation.template_engine import TemplateEngine

def main():
    # Initialize the automation system
    automation = GoogleDocsAutomation('path/to/credentials.json')
    doc_manager = DocumentManager(automation)
    template_engine = TemplateEngine()
    
    # Create a new document
    doc_id = doc_manager.create_document("Test Document")
    
    # Insert text with formatting
    doc_manager.insert_text(doc_id, "Hello, World!")
    doc_manager.apply_formatting(doc_id, 0, 12, {
        'bold': True,
        'fontSize': {'magnitude': 14, 'unit': 'PT'}
    })
    
    # Create document from template
    variables = {
        'title': 'Monthly Report',
        'author': 'John Doe',
        'content': 'This is the monthly report content.'
    }
    template_doc_id = template_engine.create_document_from_template(
        doc_manager,
        'monthly_report.j2',
        variables,
        'Generated Monthly Report'
    )

if __name__ == '__main__':
    main() 