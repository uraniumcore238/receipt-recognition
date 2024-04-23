## Local run

You will need Python 3.11+ on your local pc. Go to project package in your terminal
```
cd path_to_ptogect
```
### 1.Install poetry, requirements and environment
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
poetry install --no-dev
```
For environment variables create file with title ".env" with the same data as .env.template.
Set BASE_DOMAIN=http://127.0.0.1:8000 there
### 2.Run the server with:
```
uvicorn receipts.api:app --reload
```
### 3.Check it
Open your browser at http://127.0.0.1:8000/docs


### 4.Interactive API docs
Now go to http://127.0.0.1:8000/docs to check all requests which can be used GET, POST, UPDATE or DELETE data.

### 5.You can run tests using pytest with different options


## Run in Docker

### 1.Create docker image
From the project directory execute the command in terminal
```
docker build --tag receipts-recognition .
```
### 2. Run the docker container
```
docker run -p 8000:8000 --env-file=.env receipts-recognition
```
Now the application is started in docker container. Go to http://127.0.0.1:8000/orders/1 to check it
You will see the JSON response as:
```
{"id": 1, "product_name": "Product A", "quantity": 10}
```
### 3. Then you are able to run the tests and get allure report
#### From the project root run command.
```
pytest .
```
### Run in docker
```
docker build --tag receipts-recognition .
```
### 2. Run the docker container
```
docker run -p 8000:8000 receipts-recognition
```
Now the application is started in docker container. Go to http://127.0.0.1:8000/orders/1 to check it
You will see the JSON response as:


pytest --cov=receipts .
