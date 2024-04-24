FROM python:3.11-slim

ENV POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry"

RUN apt-get update && apt-get install --no-install-recommends -y && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
RUN pip install poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt -o requirements.txt
RUN pip install -r requirements.txt

COPY receipts /app/receipts
COPY data /app/data

CMD ["uvicorn", "receipts.api:app", "--host", "0.0.0.0"]
