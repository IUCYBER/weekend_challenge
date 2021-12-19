# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR /app
COPY . .
CMD [ "python", "main.py" ];
