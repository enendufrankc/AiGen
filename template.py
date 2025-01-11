import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define templates and their structures
templates = [
    {
        "name": "sql_chat_app",
        "files": [
            "main.py",
            "requirements.txt",
            "README.md",
            "src/sql_chat_app/__init__.py",
            "src/sql_chat_app/modules/__init__.py",
            "src/sql_chat_app/modules/agent.py",
            "src/sql_chat_app/modules/db.py",
            "src/sql_chat_app/modules/llm.py",
            "src/sql_chat_app/utils/__init__.py",
            "src/sql_chat_app/utils/common.py",
            "src/sql_chat_app/config/__init__.py",
            "src/sql_chat_app/config/configuration.py",
            "src/sql_chat_app/test/__init__.py",
            "src/sql_chat_app/entity/__init__.py",
            "src/sql_chat_app/entity/config_entity.py",
            "src/sql_chat_app/constants/__init__.py",
            "config/config.yaml",
            "params.yaml",
            "schema.yaml",
            "Dockerfile",
            "app.py",
            "research/trials_01.ipynb",
        ],
    },
    {
        "name": "pdf_chat_app",
        "files": [
            "main.py",
            "requirements.txt",
            "README.md",
            "src/pdf_chat_app/__init__.py",
            "src/pdf_chat_app/modules/__init__.py",
            "src/pdf_chat_app/modules/agent.py",
            "src/pdf_chat_app/modules/db.py",
            "src/pdf_chat_app/modules/llm.py",
            "src/pdf_chat_app/utils/__init__.py",
            "src/pdf_chat_app/utils/common.py",
            "src/pdf_chat_app/config/__init__.py",
            "src/pdf_chat_app/config/configuration.py",
            "src/pdf_chat_app/test/__init__.py",
            "src/pdf_chat_app/entity/__init__.py",
            "src/pdf_chat_app/entity/config_entity.py",
            "src/pdf_chat_app/constants/__init__.py",
            "config/config.yaml",
            "params.yaml",
            "schema.yaml",
            "Dockerfile",
            "app.py",
            "research/trials_01.ipynb",
        ],
    },
]

# Define additional project-level files
project_files = [
    "__init__.py",
    "cli.py",
    ".gitignore",
    "LICENSE",
    "README.md",
    "pyproject.toml",
    "setup.py",
    "tests/test_cli.py",
]

# Function to create directories and files
def create_files(template_list, project_files):
    # Create project-level files
    for file_path in project_files:
        full_path = Path(file_path)
        if full_path.parent:
            os.makedirs(full_path.parent, exist_ok=True)
        if not full_path.exists():
            with open(full_path, "w") as f:
                pass
            logging.info(f"Created file: {full_path}")

    # Create templates and their associated files
    for template in template_list:
        template_dir = Path(f"templates/{template['name']}")
        for file_path in template["files"]:
            full_path = template_dir / file_path
            os.makedirs(full_path.parent, exist_ok=True)
            if not full_path.exists():
                with open(full_path, "w") as f:
                    pass
                logging.info(f"Created file: {full_path}")
            else:
                logging.info(f"File already exists: {full_path}")

# Execute file creation
if __name__ == "__main__":
    create_files(templates, project_files)
