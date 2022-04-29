import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Research Design Records (RDR)
    """


@app.command()
def new():
    """
    Create new research design record.
    """
    typer.echo("Creating new rdr")


@app.command()
def init():
    """
    Initialize project with rdr.
    """
    typer.echo("Initializing project")