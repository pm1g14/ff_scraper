FROM python:3.8-slim-buster

WORKDIR /src

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .

CMD [ "python", "./app.py" ]

