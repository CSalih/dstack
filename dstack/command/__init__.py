import click

from dstack.command.docker import ssh, start, stop


@click.group()
@click.version_option()
def main():
    """dstack: wip"""
    pass


main.add_command(start)
main.add_command(stop)
main.add_command(ssh)
