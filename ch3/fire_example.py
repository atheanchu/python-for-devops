#!/usr/bin/env python
"""
Command Line Tool using fire
The fire package uses introspection of your code to create interfaces automatically.
With one line of additional code, you can interact with all of a module’s functions 
from the command-line.
"""

import fire


class Ships:
    def sail(self):
        ship_name = "Your Ship"
        print(f"{ship_name} is setting sail")

    def list(self):
        ships = ["John B", "Yankee Clipper", "Pequod"]
        print(f"Ships: {','.join(ships)}")


def sailors(greeting, name):
    message = f"{greeting} {name}"
    print(message)


class Cli:
    def __init__(self):
        self.sailor = sailors
        self.ships = Ships()


if __name__ == "__main__":
    fire.Fire(Cli)
