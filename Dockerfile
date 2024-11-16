From python:latest

WORKDIR /project

copy . /project

Run pip install -r requeriments.txt

CMD [ "python", "server.py" ]