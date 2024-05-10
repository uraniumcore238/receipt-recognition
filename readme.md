## Local run

You will need Python 3.11+ on your local PC. Go to project package in your terminal by the command
```
cd path_to_ptogect
```
### 1.Install poetry, requirements and environment
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
poetry install --no-dev
```
### 2.Run server
Execute command
```
uvicorn receipts.api:app --reload
```
### 3.Check it
Open your browser at http://127.0.0.1:8000/docs
The swagger with the endpoints should be reflected on the page

### 4.Test it
Execute command
```
pytest .
```
to run all tests on the project

## Run in Docker

### 1.Create docker image
From the project directory execute the command in terminal
```
docker-compose up
```

### 2. Run the project
```
docker-compose up
```
Now the application is started in docker container. Go to http://127.0.0.1:8000/docs to check it

## Add the project to GitHub registry
### 1. Execute the commands
```
docker login --username uraniumcore238@gmail.com --password your_password ghcr.io
```
```
docker build . -t ghcr.io/uraniumcore238/receipts:latest
```
```
docker push ghcr.io/uraniumcore238/receipts:latest
```
```
docker run ghcr.io/uraniumcore238/receipts:latest
```
