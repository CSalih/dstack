from enum import Enum
from typing import Any

import click as click


class LogLevel(Enum):
    DEBUG = "debug"


def is_verbose():
    return click.get_current_context().obj["verbose"]


def __log(message: str, level: LogLevel, **styles: Any):
    click.secho(f"[{level.name}]: {message}", styles=styles)


def debug(message: str):
    if is_verbose():
        __log(message, LogLevel.DEBUG, bg="blue", fg="white")
