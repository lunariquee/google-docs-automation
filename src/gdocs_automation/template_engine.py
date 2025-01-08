import jinja2
from typing import Dict, Any

class TemplateEngine:
    def __init__(self, template_folder: str = 'templates'):
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_folder)
        )
    
    def render_template(self, template_name: str, 
                       variables: Dict[str, Any]) -> str:
        """Render a template with provided variables"""
        template = self.env.get_template(template_name)
        return template.render(**variables)
    
    def create_document_from_template(self, doc_manager, 
                                    template_name: str,
                                    variables: Dict[str, Any],
                                    title: str) -> str:
        """Create a new document from a template"""
        content = self.render_template(template_name, variables)
        doc_id = doc_manager.create_document(title)
        doc_manager.insert_text(doc_id, content)
        return doc_id 