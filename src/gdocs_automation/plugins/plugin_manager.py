from typing import Dict, Any, Type, Optional
import importlib
import pkgutil
from pathlib import Path
import logging

class PluginManager:
    """Manages plugin discovery and loading"""
    
    def __init__(self, plugin_dir: str = 'plugins'):
        self.plugin_dir = Path(plugin_dir)
        self.plugins: Dict[str, Any] = {}
        self.logger = logging.getLogger(__name__)

    def discover_plugins(self) -> None:
        """Discover and load all plugins in the plugin directory"""
        if not self.plugin_dir.exists():
            self.logger.warning(f"Plugin directory not found: {self.plugin_dir}")
            return

        for finder, name, _ in pkgutil.iter_modules([str(self.plugin_dir)]):
            try:
                module = importlib.import_module(f".{name}", package=self.plugin_dir.name)
                if hasattr(module, 'register_plugin'):
                    self.plugins[name] = module.register_plugin()
                    self.logger.info(f"Loaded plugin: {name}")
            except Exception as e:
                self.logger.error(f"Failed to load plugin {name}: {str(e)}")

    def get_plugin(self, name: str) -> Optional[Any]:
        """Get a plugin by name"""
        return self.plugins.get(name)

    def execute_plugin(self, name: str, *args, **kwargs) -> Any:
        """Execute a plugin with given arguments"""
        plugin = self.get_plugin(name)
        if plugin is None:
            raise ValueError(f"Plugin not found: {name}")
        return plugin.execute(*args, **kwargs) 