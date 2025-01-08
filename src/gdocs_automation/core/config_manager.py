import yaml
from pathlib import Path
from typing import Any, Dict
import logging

class ConfigManager:
    """Manages configuration settings for the application"""
    
    def __init__(self, config_path: str = 'config/default_config.yaml'):
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = {}
        self.logger = logging.getLogger(__name__)
        self.load_config()

    def load_config(self) -> None:
        """Load configuration from YAML file"""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r') as f:
                    self.config = yaml.safe_load(f)
                self.logger.info(f"Configuration loaded from {self.config_path}")
            else:
                self.logger.warning(f"Config file not found at {self.config_path}")
                self._create_default_config()
        except Exception as e:
            self.logger.error(f"Error loading config: {str(e)}")
            self._create_default_config()

    def _create_default_config(self) -> None:
        """Create default configuration"""
        self.config = {
            'document': {
                'default_font': 'Arial',
                'default_font_size': 11,
                'default_margin': 1.0
            },
            'templates': {
                'path': 'templates',
                'default_extension': '.j2'
            },
            'logging': {
                'level': 'INFO',
                'file': 'logs/gdocs_automation.log'
            }
        }
        self._save_config()

    def _save_config(self) -> None:
        """Save current configuration to file"""
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, 'w') as f:
                yaml.dump(self.config, f)
            self.logger.info(f"Configuration saved to {self.config_path}")
        except Exception as e:
            self.logger.error(f"Error saving config: {str(e)}")

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key"""
        try:
            keys = key.split('.')
            value = self.config
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default

    def set(self, key: str, value: Any) -> None:
        """Set configuration value"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            config = config.setdefault(k, {})
        config[keys[-1]] = value
        self._save_config() 