import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

<<<<<<< HEAD
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
    "README.md",
    "LICENSE",
    ".gitignore",
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
        template_dir = Path(f"aigent_lib/templates/{template['name']}")
        for file_path in template["files"]:
            full_path = template_dir / file_path
            os.makedirs(full_path.parent, exist_ok=True)
            if not full_path.exists():
                with open(full_path, "w") as f:
                    pass
                logging.info(f"Created file: {full_path}")

# Execute file creation
if __name__ == "__main__":
    create_files(templates, project_files)
=======
template1_name = "sql_chat_app"
template2_name = "pdf_chat_app"

list_of_files = [
    "__init__.py",
    "cli.py",
    f"templates/{template1_name}/main.py",
    ".github/workflows/.gitkeep",
    f"templates/{template1_name}/src/{template1_name}/__init__.py",
    f"templates/{template1_name}/src/{template1_name}/modules/__init__.py",
    f"templates/{template1_name}/src/{template1_name}/modules/agent.py",
    f"templates/{template1_name}/src/{template1_name}/modules/db.py",
    f"templates/{template1_name}/src/{template1_name}/modules/llm.py",
    f"templates/{template1_name}/src/{template1_name}/modules/pdf_generator.py",
    f"templates/{template1_name}/src/{template1_name}/utils/__init__.py",
    f"templates/{template1_name}/src/{template1_name}/utils/common.py",
    f"templates/{template1_name}/src/{template1_name}/config/__init__.py",
    f"templates/{template1_name}/src/{template1_name}/config/configuration.py",
    f"templates/{template1_name}/src/{template1_name}/test/__init__.py",
    f"templates/{template1_name}/src/{template1_name}/entity/__init__.py",
    f"templates/{template1_name}/src/{template1_name}/entity/config_entity.py",
    f"templates/{template1_name}/src/{template1_name}/constants/__init__.py",
    f"templates/{template1_name}/config/config.yaml",
    f"templates/{template1_name}/params.yaml",
    f"templates/{template1_name}/schema.yaml",
    f"templates/{template1_name}/main.py",
    f"templates/{template1_name}/app.py",
    f"templates/{template1_name}/Dockerfile",
    f"templates/{template1_name}/requirements.txt",
    f"templates/{template1_name}/README.md",
    f"templates/{template1_name}/research/trials_01.ipynb",
    f"templates/{template2_name}/src/{template2_name}/__init__.py",
    f"templates/{template2_name}/src/{template2_name}/modules/__init__.py",
    f"templates/{template2_name}/src/{template2_name}/modules/agent.py",
    f"templates/{template2_name}/src/{template2_name}/modules/db.py",
    f"templates/{template2_name}/src/{template2_name}/modules/llm.py",
    f"templates/{template2_name}/src/{template2_name}/modules/pdf_generator.py",
    f"templates/{template2_name}/src/{template2_name}/utils/__init__.py",
    f"templates/{template2_name}/src/{template2_name}/utils/common.py",
    f"templates/{template2_name}/src/{template2_name}/config/__init__.py",
    f"templates/{template2_name}/src/{template2_name}/config/configuration.py",
    f"templates/{template2_name}/src/{template2_name}/test/__init__.py",
    f"templates/{template2_name}/src/{template2_name}/entity/__init__.py",
    f"templates/{template2_name}/src/{template2_name}/entity/config_entity.py",
    f"templates/{template2_name}/src/{template2_name}/constants/__init__.py",
    f"templates/{template2_name}/config/config.yaml",
    f"templates/{template2_name}/params.yaml",
    f"templates/{template2_name}/schema.yaml",
    f"templates/{template2_name}/main.py",
    f"templates/{template2_name}/app.py",
    f"templates/{template2_name}/Dockerfile",
    f"templates/{template2_name}/requirements.txt",
    f"templates/{template2_name}/README.md",
    f"templates/{template2_name}/research/trials_01.ipynb",
    "tests/test_cli.py",
    "setup.py",
    "README.md",
    "LICENSE",
    ".gitignore",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials_01.ipynb",
    "test.py"
]

def create_files(file_list):
    for file_path in file_list:
        full_path = Path(file_path)
        filedir, filename = os.path.split(full_path)

        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file: {filename}")

        if not os.path.exists(full_path) or os.path.getsize(full_path) == 0:
            with open(full_path, "w") as f:
                pass
            logging.info(f"Creating empty file: {full_path}")
        else:
            logging.info(f"{filename} already exists")

if __name__ == "__main__":
    create_files(list_of_files)
>>>>>>> 321da561b23bd63b26ce2a1f5955630d74dad073
