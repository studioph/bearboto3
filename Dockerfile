ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

RUN pip3 install poetry

COPY poetry.lock pyproject.toml /tmp/

WORKDIR /tmp

RUN poetry install --remove-untracked

VOLUME /repo

WORKDIR /repo

CMD poetry shell