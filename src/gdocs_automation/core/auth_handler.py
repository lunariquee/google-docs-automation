from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from typing import Optional
import os.path
import pickle
import logging

class AuthHandler:
    """Handles OAuth2 authentication with Google APIs"""
    
    SCOPES = [
        'https://www.googleapis.com/auth/documents',
        'https://www.googleapis.com/auth/drive'
    ]
    
    def __init__(self, credentials_path: str, token_path: str = 'token.pickle'):
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.credentials: Optional[Credentials] = None
        self.logger = logging.getLogger(__name__)

    def authenticate(self) -> Credentials:
        """Perform authentication flow and return credentials"""
        if os.path.exists(self.token_path):
            self.logger.debug("Loading existing token")
            with open(self.token_path, 'rb') as token:
                self.credentials = pickle.load(token)

        if not self.credentials or not self.credentials.valid:
            self.credentials = self._refresh_credentials()
            
        return self.credentials

    def _refresh_credentials(self) -> Credentials:
        """Refresh or obtain new credentials"""
        if self.credentials and self.credentials.expired and self.credentials.refresh_token:
            self.logger.info("Refreshing expired credentials")
            self.credentials.refresh(Request())
        else:
            self.logger.info("Initiating new authentication flow")
            flow = InstalledAppFlow.from_client_secrets_file(
                self.credentials_path, self.SCOPES)
            self.credentials = flow.run_local_server(port=0)

        self.logger.debug("Saving new token")
        with open(self.token_path, 'wb') as token:
            pickle.dump(self.credentials, token)

        return self.credentials 