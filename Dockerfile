FROM python:3.11-slim


ENV POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry"


RUN apt-get update && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

# Set the working directory inside the container
WORKDIR /app

# Copy only the dependency-related files to leverage Docker layer caching
COPY pyproject.toml poetry.lock ./

# Install dependencies (excluding dev dependencies)
RUN poetry install --no-dev

COPY receipts /app/receipts
COPY tests /app/tests
COPY data /app/data

CMD ["poetry", "run", "uvicorn", "receipts.api:app", "--host", "0.0.0.0"]
