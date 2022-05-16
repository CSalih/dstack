import click
from click import Context

from dstack.command.docker import ssh, start, stop


@click.group(invoke_without_command=True)
@click.version_option()
@click.option('-v', '--verbose', is_flag=True, help='Enables verbose mode', default=False)
@click.pass_context
def main(ctx: Context, verbose: bool):
    """
    A cli tool to manage your local stack.
    """
    ctx.obj = {
        "verbose": verbose
    }

    if ctx.invoked_subcommand is None:
        ctx.invoke(ssh)

    pass


main.add_command(start)
main.add_command(stop)
main.add_command(ssh)
