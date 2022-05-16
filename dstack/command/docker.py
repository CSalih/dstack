import os

import click
import docker

from dstack import DOCKER_PROJECT_NAME, DOCKER_COMPOSE_FILE_PATH


def docker_compose(args: str):
    click.echo(f'docker-compose {args}')
    os.system(f'docker-compose -p "{DOCKER_PROJECT_NAME}" -f "{DOCKER_COMPOSE_FILE_PATH}" {args}')


@click.command()
def ssh():
    """SSH into the docker stack."""
    docker_client = docker.from_env()
    is_running = docker_client.api.containers(filters={"status": "running", "name": "ez_cli"})
    if not is_running:
        docker_compose('start')

    # TODO: workdir should allowed only when the directory is mapped as volume
    # workdir = f"/{os.path.basename(os.getcwd())}"
    # docker_compose(f'exec --workdir="/var/www{workdir}" --user site cli bash')
    docker_compose('exec --user site cli bash')


@click.command()
def start():
    """Start the docker stack."""
    docker_compose('start')


@click.command()
def stop():
    """Stop the docker stack."""
    docker_compose('stop')
