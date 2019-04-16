# -*- coding: utf-8 -*-

"""Console script for mbta_py."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for mbta_py."""
    click.echo("Replace this message by putting your code into "
               "mbta.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0

@click.group()
def predict():
    pass


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
