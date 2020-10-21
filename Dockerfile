FROM python:3.8

COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 8000/tcp
CMD uvicorn server:app --loop uvloop --host 0.0.0.0 --port 8000
