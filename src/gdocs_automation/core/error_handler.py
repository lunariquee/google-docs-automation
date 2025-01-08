from typing import Type, Callable, Any, Tuple
import logging
import functools

class GDocsAutomationError(Exception):
    """Base exception class for GDocs Automation"""
    pass

class AuthenticationError(GDocsAutomationError):
    """Raised when authentication fails"""
    pass

class DocumentError(GDocsAutomationError):
    """Raised when document operations fail"""
    pass

class TemplateError(GDocsAutomationError):
    """Raised when template operations fail"""
    pass

def handle_errors(
    error_types: Tuple[Type[Exception], ...] = (Exception,),
    logger: logging.Logger = None,
    default_return: Any = None
) -> Callable:
    """
    Decorator for handling errors in functions
    
    Args:
        error_types: Tuple of exception types to catch
        logger: Logger instance to use
        default_return: Value to return on error
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal logger
            if logger is None:
                logger = logging.getLogger(func.__module__)
            
            try:
                return func(*args, **kwargs)
            except error_types as e:
                logger.error(f"Error in {func.__name__}: {str(e)}")
                if isinstance(e, GDocsAutomationError):
                    raise
                return default_return
                
        return wrapper
    return decorator 