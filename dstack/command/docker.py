import click
import docker

from dstack.utils.docker_compose import docker_compose
from dstack.utils.logger import debug


def is_stack_running() -> bool:
    docker_client = docker.from_env()
    return docker_client.api.containers(filters={"status": "running", "name": "ez_cli"})


@click.command()
def ssh():
    """SSH into the docker stack."""
    if not is_stack_running():
        debug("Stack is not running. Try to start the stack ...")
        docker_compose("start")

    # TODO: workdir should allowed only when the directory is mapped as volume
    # workdir = f"/{os.path.basename(os.getcwd())}"
    # docker_compose(f'exec --workdir="/var/www{workdir}" --user site cli bash')
    docker_compose("exec --user site cli bash")


@click.command()
def start():
    """Start the docker stack."""
    docker_compose("start")


@click.command()
def stop():
    """Stop the docker stack."""
    docker_compose("stop")
