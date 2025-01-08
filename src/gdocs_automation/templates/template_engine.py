from typing import Dict, Any, Optional
from jinja2 import Environment, FileSystemLoader, Template
from pathlib import Path
import logging
from ..core.error_handler import handle_errors, TemplateError

class TemplateEngine:
    """Handles document template processing"""
    
    def __init__(self, template_dir: str = 'templates'):
        self.template_dir = Path(template_dir)
        self.env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            autoescape=True,
            trim_blocks=True,
            lstrip_blocks=True
        )
        self.logger = logging.getLogger(__name__)

    @handle_errors(error_types=(Exception,))
    def get_template(self, template_name: str) -> Template:
        """Load a template by name"""
        try:
            return self.env.get_template(template_name)
        except Exception as e:
            raise TemplateError(f"Failed to load template {template_name}: {str(e)}")

    @handle_errors(error_types=(Exception,))
    def render(self, template_name: str, context: Dict[str, Any]) -> str:
        """Render a template with provided context"""
        template = self.get_template(template_name)
        try:
            return template.render(**context)
        except Exception as e:
            raise TemplateError(f"Failed to render template {template_name}: {str(e)}")

    @handle_errors(error_types=(Exception,))
    def create_template(self, name: str, content: str) -> None:
        """Create a new template file"""
        template_path = self.template_dir / name
        template_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(template_path, 'w') as f:
                f.write(content)
            self.logger.info(f"Created template: {name}")
        except Exception as e:
            raise TemplateError(f"Failed to create template {name}: {str(e)}") 