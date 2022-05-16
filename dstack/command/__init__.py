import click

from dstack.command.docker import ssh, start, stop


@click.group()
@click.version_option()
@click.option('-v', '--verbose', is_flag=True, help='Enables verbose mode', default=False)
@click.pass_context
def main(ctx, verbose: bool):
    ctx.obj = {
        "verbose": verbose
    }

    """dstack: wip"""
    pass


main.add_command(start)
main.add_command(stop)
main.add_command(ssh)
