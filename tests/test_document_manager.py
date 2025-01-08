import pytest
from gdocs_automation.document.document_manager import DocumentManager
from unittest.mock import MagicMock, create_autospec, patch
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def test_create_document():
    # Mock credentials with universe_domain
    mock_creds = MagicMock(spec=Credentials)
    mock_creds.universe_domain = "googleapis.com"
    
    # Create mock service
    mock_service = MagicMock()
    mock_docs = MagicMock()
    mock_create = MagicMock()
    mock_create.execute.return_value = {'documentId': 'test_doc_id'}
    
    mock_docs.create.return_value = mock_create
    mock_service.documents.return_value = mock_docs
    
    # Patch the build function
    with patch('googleapiclient.discovery.build', return_value=mock_service):
        # Create DocumentManager instance
        doc_manager = DocumentManager(mock_creds)
        
        # Test document creation
        doc_id = doc_manager.create_document("Test Document")
        assert doc_id == 'test_doc_id'
        
        # Verify the service was called correctly
        mock_docs.create.assert_called_once_with(
            body={'title': 'Test Document'}
        )

def test_insert_text():
    # Mock credentials with universe_domain
    mock_creds = MagicMock(spec=Credentials)
    mock_creds.universe_domain = "googleapis.com"
    
    # Create mock service
    mock_service = MagicMock()
    mock_docs = MagicMock()
    mock_batch_update = MagicMock()
    mock_batch_update.execute.return_value = {}
    
    mock_docs.batchUpdate.return_value = mock_batch_update
    mock_service.documents.return_value = mock_docs
    
    # Patch the build function
    with patch('googleapiclient.discovery.build', return_value=mock_service):
        # Create DocumentManager instance
        doc_manager = DocumentManager(mock_creds)
        
        # Test text insertion
        doc_manager.insert_text('test_doc_id', 'Hello World')
        
        # Verify the service was called correctly
        mock_docs.batchUpdate.assert_called_once_with(
            documentId='test_doc_id',
            body={'requests': [{
                'insertText': {
                    'location': {'index': 1},
                    'text': 'Hello World'
                }
            }]}
        ) 