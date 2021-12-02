FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
pytest --cov=. tests.py
CMD [ "pytest", "--cov=." , "tests.py"]
