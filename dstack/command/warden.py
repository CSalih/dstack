import os

import click

from dstack.utils.logger import debug


def warden(args: str):
    """Helper to execute warden (https://github.com/wardenenv/warden)"""
    debug(f"warden {args}")
    os.system(f'warden {args}')


@click.command()
def ssh():
    """Connect to the cli."""
    warden("shell")


@click.command()
def start():
    """Start the warden environment."""
    warden("env up")


@click.command()
def stop():
    """Stop the warden environment."""
    warden("env stop")
