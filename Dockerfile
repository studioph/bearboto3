ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

RUN pip3 install poetry

COPY . /repo

WORKDIR /repo

RUN poetry install

CMD poetry shell