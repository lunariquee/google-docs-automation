import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_credentials():
    return MagicMock()

@pytest.fixture
def mock_docs_service():
    service = MagicMock()
    service.documents().create().execute.return_value = {'documentId': 'test_doc_id'}
    return service 