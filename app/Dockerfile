FROM python:3.12-alpine

WORKDIR /app 

RUN apk update --no-cache && apk add --no-cache bash

COPY . .

CMD ["python3", "script.py"]
