#!/usr/bin/env python
"""
A simple application that discovers and runs plug-ins
"""
import fire
import pkgutil
import importlib
import sys

print(sys.path)


def find_and_run_plugins(prefix):
    plugins = {}

    print(f"Discovering plugins with prefix: {prefix}")

    # pkgutil.iter_modules returns all modules available in the current sys.path
    for _, name, _ in pkgutil.iter_modules():
        if name.startswith(prefix):
            module = importlib.import_module(name)
            plugins["name"] = module

    for name, module in plugins.items():
        print(f"Running plugin {name}")
        module.run()


if __name__ == "__main__":
    fire.Fire()
