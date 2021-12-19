# syntax=docker/dockerfile:1
FROM alpine
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
WORKDIR /app
COPY . .
CMD [ "sh", "run_tests.sh" ];