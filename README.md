# Google Docs Automation System

An advanced, open-source system for automating Google Docs operations with Python. This project provides a flexible and extensible framework for creating, modifying, and managing Google Documents programmatically.

## Features

- 🔐 Secure OAuth2 authentication with token persistence
- 📄 Create and modify Google Docs programmatically
- 🎨 Advanced text formatting capabilities
- 📋 Template-based document generation using Jinja2
- 🔧 Modular and extensible architecture
- 📝 Type hints for better code maintainability

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/gdocs-automation.git
cd gdocs-automation
```

2. Install required dependencies:
```bash
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client jinja2
```

## Setup

1. Create a Google Cloud Project at [Google Cloud Console](https://console.cloud.google.com)
2. Enable the Google Docs API and Google Drive API
3. Create OAuth 2.0 credentials and download the `credentials.json` file
4. Place the `credentials.json` file in your project root directory

## Project Structure

```
gdocs-automation/
├── src/
│   └── gdocs_automation/
│       ├── __init__.py
│       ├── core.py
│       ├── document_manager.py
│       └── template_engine.py
├── examples/
│   └── usage_example.py
├── templates/
│   └── monthly_report.j2
├── credentials.json
└── README.md
```

## Usage

Here's a basic example of how to use the system:

```python
from gdocs_automation.core import GoogleDocsAutomation
from gdocs_automation.document_manager import DocumentManager
from gdocs_automation.template_engine import TemplateEngine

# Initialize the automation system
automation = GoogleDocsAutomation('path/to/credentials.json')
doc_manager = DocumentManager(automation)
template_engine = TemplateEngine()

# Create a new document
doc_id = doc_manager.create_document("Test Document")

# Insert text with formatting
doc_manager.insert_text(doc_id, "Hello, World!")
doc_manager.apply_formatting(doc_id, 0, 12, {
    'bold': True,
    'fontSize': {'magnitude': 14, 'unit': 'PT'}
})
```

## Template Usage

1. Create a template file in the `templates` directory:

```jinja
# {{title}}
Author: {{author}}

{{content}}
```

2. Use the template engine to generate documents:

```python
variables = {
    'title': 'Monthly Report',
    'author': 'John Doe',
    'content': 'This is the monthly report content.'
}

template_doc_id = template_engine.create_document_from_template(
    doc_manager,
    'monthly_report.j2',
    variables,
    'Generated Monthly Report'
)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Docs API
- Google Drive API
- Jinja2 Template Engine

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Future Enhancements

- Batch document processing
- Advanced formatting options
- Document sharing and permissions management
- Image handling and manipulation
- Table creation and management
- Real-time collaboration features