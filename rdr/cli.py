import os
import sys
import typer
from pathlib import Path
from typing import Optional
import confuse
import frontmatter
from rich.console import Console
from rich.markdown import Markdown
from rdr import utils
# from rdr.tasks import list_resources
from rdr.tasks import make_rdr_md
from rdr.tasks import read_rdr_md
from rdr.tasks import list_resources
from rdr.tasks import view_md


from logbook import Logger, StreamHandler
StreamHandler(sys.stdout).push_application()
log = Logger('RDR')

from rdr import utils

CONFIG_NAME="rdr.yaml"

app = typer.Typer()

@app.callback()
def callback():
    """
    Research Design Records (RDR)
    """

@app.command()
def init(path: str = ".", overwrite: bool = False):
    """
    Initialize a new RDR project.
    """
    typer.echo("Initializing project")

    # test if config file already exists
    config_file = utils.search_upwards_for_file(CONFIG_NAME)
    if config_file:
        log.warn(f"An existing rdr configuration is detected at: {config_file}")
        if overwrite:
            typer.echo("Overwriting!")
        else:
            raise typer.Abort()

    # this should create the config file
    config = confuse.Configuration('rdr', __name__)

    with open(os.path.join(path, CONFIG_NAME), 'w') as fh:
        fh.write(config.dump())
        log.info(f"Configuration created at: {os.path.join(path, CONFIG_NAME)}")

    # create directories
    for dir_name in ['rdr-path','mp-path','dp-path','ep-path']:
        log.info(f"Creating directory: {config[dir_name].as_filename()}")
        Path(config[dir_name].as_filename()).mkdir(parents=True, exist_ok=True)

@app.command()
def ls():
    """
    List resources in the project.

    """
    typer.echo("Listing all records and protocols")

    # TODO: load configuration
    log.info("This is a test")
    config_file = utils.search_upwards_for_file(CONFIG_NAME)
    if not config_file:
        typer.echo("No existing RDR configuration is detected.")
        raise typer.Abort()    
    config = confuse.Configuration('rdr', __name__)
    config.set_file(config_file, base_for_paths=True)

    # list all Markdown files under path
    directory = Path(config['rdr-path'].as_filename())
    listing = list(directory.glob('*.md'))

    # for resource in [_.name for _ in listing]:
    #     typer.echo(resource)

    list_resources(listing)

@app.command()
def view(name: str):
    """
    View a resource in the terminal.
    """
    typer.echo("Listing all records and protocols")

    # TODO: load configuration
    log.info("This is a test")
    config_file = utils.search_upwards_for_file(CONFIG_NAME)
    if not config_file:
        typer.echo("No existing RDR configuration is detected.")
        raise typer.Abort()    
    config = confuse.Configuration('rdr', __name__)
    config.set_file(config_file, base_for_paths=True)

    file = Path(config['rdr-path'].as_filename(), f"{name}.md")
    if file.exists():
        # render markdown content to terminal
        # md_text = read_rdr_md(file)

        with open(file) as f:
            post = frontmatter.load(f)
            # md_text = file.read_text()
            console = Console()
            md = Markdown(post.content)
            console.print(md)        
    else:
        typer.echo(f"{name} does not exist!")
        raise typer.Abort()
    
    view_md(file)

@app.command()
def new(title: str):
    """
    Create new research design record.
    """
    typer.echo("Creating new rdr")

    # TODO: load configuration
    conf_path = utils.search_upwards_for_file(CONFIG_NAME)
    if not conf_path:
        typer.echo("No existing RDR configuration is detected.")
        raise typer.Abort()    
    config = confuse.Configuration('rdr', __name__)
    config.set_file(conf_path, base_for_paths=True)

    # TODO: load rdr index
    directory = Path(config['rdr-path'].as_filename())
    listing = list(directory.glob('*.md'))
    if listing:
        last = max(listing)
        idx = int ( ''.join(filter(str.isdigit, last.name) ) ) + 1
    else:
        idx = 1
    next_id = f"RDR-{idx:0>4}"

    # TODO: generate next rdr id
    new_rdr_path = os.path.join(config['rdr-path'].as_filename(), next_id)

    # TODO: generate new rdr file
    log.info(f"created: {new_rdr_path}.md")
    make_rdr_md(
        path = config['rdr-path'].as_filename(), 
        name = next_id, 
        title = title)

@app.command()
def add(rdr: str, protocol: str):
    """
    Add a protocol to a research design record.
    """
    typer.echo("Creating new rdr")

    # TODO: load configuration

@app.command()
def compile():
    """
    Compiles the research design.
    """
    typer.echo("Creating new rdr")