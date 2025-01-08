"""Core functionality for Google Docs Automation."""
from .error_handler import (
    GDocsAutomationError,
    AuthenticationError,
    DocumentError,
    TemplateError,
    handle_errors
)
from .automation import GoogleDocsAutomation

__all__ = [
    'GoogleDocsAutomation',
    'GDocsAutomationError',
    'AuthenticationError',
    'DocumentError',
    'TemplateError',
    'handle_errors'
] 