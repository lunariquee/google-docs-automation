"""Core functionality for Google Docs Automation."""
from .error_handler import (
    GDocsAutomationError,
    AuthenticationError,
    DocumentError,
    TemplateError,
    handle_errors
) 