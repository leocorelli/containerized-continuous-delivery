import click
import numpy as np


@click.command()
@click.option("--n", prompt="First n squares")
def list_squares(n: int):
    for i in range(1, int(n) + 1):
        click.echo(f"{int(i)}: {np.power(int(i),2)}")
        if int(i) == int(n):
            click.echo("\nDone!\n")


if __name__ == "__main__":
    list_squares()