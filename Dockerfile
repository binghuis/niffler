ARG PYTHON_BASE=3.13-slim

# 构建阶段
FROM python:$PYTHON_BASE AS builder

RUN pip install -U pdm
ENV PDM_CHECK_UPDATE=false

WORKDIR /project

COPY pyproject.toml pdm.lock README.md ./

RUN pdm install --check --prod --no-editable

# 运行阶段
FROM python:$PYTHON_BASE

WORKDIR /project

COPY --from=builder /project/.venv/ ./.venv
ENV PATH="/project/.venv/bin:$PATH"

ENV PYTHONPATH="/project/src:$PYTHONPATH"

COPY src ./src

CMD ["uvicorn", "niffler.main:app", "--host", "0.0.0.0", "--port", "8000"]
