# aigent_lib/cli.py

import os
import shutil
import click

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")

@click.group()
def cli():
    """Aigent CLI: Generate AI projects from templates."""
    pass

@cli.command()
def list_templates():
    """
    List all available templates.
    """
    templates = [
        d for d in os.listdir(TEMPLATES_DIR)
        if os.path.isdir(os.path.join(TEMPLATES_DIR, d))
    ]
    click.echo("Available templates:")
    for template in templates:
        click.echo(f" - {template}")

@cli.command()
@click.argument("template_name")
@click.argument("project_name")
def create(template_name, project_name):
    """
    Create a new AI project from a template.

    Usage:
    aigent create <template_name> <project_name>
    """
    src_path = os.path.join(TEMPLATES_DIR, template_name)
    if not os.path.exists(src_path):
        click.echo(f"Template '{template_name}' does not exist.")
        return

    if os.path.exists(project_name):
        click.echo(f"Directory '{project_name}' already exists.")
        return

    shutil.copytree(src_path, project_name)
    click.echo(f"Project '{project_name}' created successfully from '{template_name}'!")

if __name__ == "__main__":
    cli()
