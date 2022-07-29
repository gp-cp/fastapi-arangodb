FROM bitnami/python:3.10 as base

FROM base as builder

WORKDIR /build

ARG DEBIAN_FRONTEND=noninteractive

# Python env
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random

# PIP settings
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && poetry export --without-hashes -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . ./

RUN poetry build && /venv/bin/pip install dist/*.whl

FROM bitnami/python:3.10-prod as runner

RUN useradd --create-home app
COPY --from=builder /venv /venv

WORKDIR /home/app

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/venv
ENV PATH="/venv/bin:$PATH"

EXPOSE 8000

RUN chown -R app:app /home/app

USER app

CMD uvicorn app.main:server 
