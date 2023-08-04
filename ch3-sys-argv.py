#!/usr/bin/env python
"""
Simple command-line tool using sys.argv
"""
import sys


def say_it(greeting, target):
    print(f"{greeting} {target}")


if __name__ == "__main__":
    # if there are --help argument, show help message
    if "--help" in sys.argv:
        print(f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>")
        sys.exit()

    if "--name" in sys.argv:
        # Get the argument after --name
        name_index = sys.argv.index("--name") + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]

    if "--greeting" in sys.argv:
        # Get the argument after --name
        greeting_index = sys.argv.index("--greeting") + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    say_it(greeting, name)
