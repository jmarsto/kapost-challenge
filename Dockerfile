FROM python:2

COPY script.py /script.py

RUN pip install boto3

ENTRYPOINT ["python", "script.py", "yellowstonejm123", "yellowstonejm1234", ".002"]
