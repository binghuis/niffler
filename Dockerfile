FROM python:3.13-slim

RUN pip install --no-cache-dir pdm

WORKDIR /app

COPY . .

RUN pdm install --production --no-cache

CMD ["pdm", "prod"]
