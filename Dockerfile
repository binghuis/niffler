ARG PYTHON_BASE=3.13-slim

# Build stage
FROM python:$PYTHON_BASE AS builder

RUN pip install -U pdm
ENV PDM_CHECK_UPDATE=false

WORKDIR /project

COPY pyproject.toml pdm.lock README.md ./

RUN pdm install --check --prod --no-editable

# Run stage
FROM python:$PYTHON_BASE

WORKDIR /project

COPY --from=builder /project/.venv/ ./.venv
ENV PATH="/project/.venv/bin:$PATH"

ENV PYTHONPATH="/project/src:$PYTHONPATH"

COPY src /project/src

CMD ["python", "src/niffler/__main__.py"]
