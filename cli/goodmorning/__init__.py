import click

@click.command()
@click.option("--name", default=None, help="Introduce yourself")
def say_goodmorning(name: str) -> None:
    if name:
        click.echo(f"Good Morning, {name}!")
    else:
        click.echo("Hello There!")