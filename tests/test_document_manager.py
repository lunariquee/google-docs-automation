import pytest
from gdocs_automation.document.document_manager import DocumentManager
from unittest.mock import MagicMock
from google.oauth2.credentials import Credentials

def test_create_document():
    # Mock credentials
    mock_creds = MagicMock(spec=Credentials)
    
    # Create DocumentManager instance with mocked services
    doc_manager = DocumentManager(mock_creds)
    doc_manager.service.documents().create().execute.return_value = {
        'documentId': 'test_doc_id'
    }
    
    # Test document creation
    doc_id = doc_manager.create_document("Test Document")
    assert doc_id == 'test_doc_id'
    
    # Verify the service was called correctly
    doc_manager.service.documents().create.assert_called_once_with(
        body={'title': 'Test Document'}
    )

def test_insert_text():
    # Mock credentials
    mock_credentials = MagicMock()
    
    # Create DocumentManager instance
    doc_manager = DocumentManager(mock_credentials)
    
    # Test text insertion
    doc_manager.insert_text('test_doc_id', 'Hello World')
    
    # Verify the service was called correctly
    doc_manager.service.documents().batchUpdate.assert_called_once() 