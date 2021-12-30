ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

RUN pip3 install poetry

COPY poetry.lock pyproject.toml /tmp/

RUN poetry config virtualenvs.create false

WORKDIR /tmp

RUN poetry install --remove-untracked

CMD poetry shell