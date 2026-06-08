import typer

from .nigel import nigel


app = typer.Typer()
app.command()(nigel)


if __name__ == "__main__":
    app()

