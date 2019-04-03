FROM python:2

COPY script.py /script.py

RUN pip install boto3

CMD ["python", "/script.py"]
