import logging
import sys
from pathlib import Path
from typing import Optional


class LoggerSetup:
    """Configure logging for the application"""

    @staticmethod
    def setup(
        log_level: int = logging.INFO,
        log_file: Optional[str] = None,
        log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    ) -> None:
        """
        Set up logging configuration

        Args:
            log_level: Logging level (default: INFO)
            log_file: Optional file path for logging
            log_format: Format string for log messages
        """
        # Create logger
        root_logger = logging.getLogger()
        root_logger.setLevel(log_level)

        # Create formatter
        formatter = logging.Formatter(log_format)

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)

        # File handler (if specified)
        if log_file:
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)

            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            root_logger.addHandler(file_handler) 