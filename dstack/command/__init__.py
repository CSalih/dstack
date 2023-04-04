import os

import click
from click import Context
from dotenv import load_dotenv

from dstack.command import docker
from dstack.command import warden

load_dotenv("{}/.env".format(os.getcwd()))
is_warden = os.getenv('WARDEN_ENV_NAME') is not None


@click.group(invoke_without_command=True)
@click.version_option()
@click.option(
    "-v", "--verbose", is_flag=True, help="Enables verbose mode", default=False
)
@click.pass_context
def main(ctx: Context, verbose: bool):
    """
    A cli tool to manage your local stack.
    """
    ctx.obj = {"verbose": verbose}

    if ctx.invoked_subcommand is None:
        ctx.invoke(docker.ssh)

    pass


if is_warden:
    main.add_command(warden.ssh)
    main.add_command(warden.start)
    main.add_command(warden.stop)
else:
    main.add_command(docker.start)
    main.add_command(docker.stop)
    main.add_command(docker.ssh)
