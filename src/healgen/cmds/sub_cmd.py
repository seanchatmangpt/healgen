"""Generating subcommands."""
import typer
# You can customize the content of the module here
from jinja2 import Template

from healgen.utils.path_tools import src_dir, cmds_dir

app = typer.Typer(help="Subcommand to generate subcommands")

subcommand_template = '''"""{{ subcommand_name }}"""
import typer


app = typer.Typer()


@app.command(name="{{ new_command_name }}")
def {{ sub_command_name }}_{{ new_command_name }}():
    """{{ new_command_name }}"""
    typer.echo("Running {{ new_command_name }} subcommand.")

'''


@app.command(name="new")
def cmd_new(subcommand_name: str = typer.Argument(..., help="The name of the new subcommand"),
            new_command_name: str = typer.Argument("new", help="The name of the new command within the subcommand")):
    """Creates a new subcommand with the command name and subcommand"""

    # Generate the filename for the new subcommand module
    filename = f"{subcommand_name}_cmd.py"
    module_path = cmds_dir() / filename

    # Check if the existing subcommand module file exists
    if module_path.exists():
        typer.echo(f"Subcommand module '{subcommand_name}' already exists.")
        return

    # Create the subcommand module file
    with open(cmds_dir() / filename, "w") as file:
        # Create a Jinja2 template from the subcommand_template string
        template = Template(subcommand_template)

        # Render the template with the provided subcommand_name and new_command_name
        source = template.render(subcommand_name=subcommand_name,
                                 new_command_name=new_command_name,
                                 sub_command_name=subcommand_name)
        file.write(source)

    typer.echo(f"Subcommand module '{subcommand_name}' generated successfully!")


@app.command(name="list")
def cmd_list(subcommand_name: str):
    ...
