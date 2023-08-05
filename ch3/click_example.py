#!/usr/bin/env python
"""
Command-line tool using click
"""

import click


# Decorator to create a top-level group
@click.group()
def cli():
    pass


@click.group()
def ships():
    pass


cli.add_command(ships)


@ships.command(help="Sail a ship")
def sail():
    ship_name = "Your Ship"
    print(f"{ship_name} is setting sail")


@ships.command(help="List all of the ships")
def list_ships():
    ships = ["John B", "Yankee Clipper", "Pequod"]
    print(f"Ships: {','.join(ships)}")


@cli.command(help="Talk to a sailor")
@click.option("--greeting", default="Ahoy there", help="Greeting for a sailor")
@click.argument("name")
def sailor(greeting, name):
    message = f"{greeting} {name}"
    print(message)


if __name__ == "__main__":
    cli()
