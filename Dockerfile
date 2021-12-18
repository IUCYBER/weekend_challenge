FROM python:alpine

COPY . .

CMD ["python3", "./main_test.py"]