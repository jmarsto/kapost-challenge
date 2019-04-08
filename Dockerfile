FROM python:2

COPY script.py /script.py

RUN pip install boto3

ENTRYPOINT ["python", "script.py", "source_bucket_name", "destination_bucket_name", "threshold_in_mb"]
