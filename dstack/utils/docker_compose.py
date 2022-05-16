import os

from dstack import DOCKER_COMPOSE_FILE_PATH, DOCKER_PROJECT_NAME
from dstack.utils.logger import debug


def docker_compose(args: str):
    debug(f"docker-compose {args}")
    os.system(
        f'docker-compose -p "{DOCKER_PROJECT_NAME}" -f "{DOCKER_COMPOSE_FILE_PATH}" {args}'
    )
