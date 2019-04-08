FROM python:2

COPY script.py /script.py

RUN pip install boto3

ENTRYPOINT ["python", "script.py", "yellowstone123", "yellowstone1234", ".002"]
