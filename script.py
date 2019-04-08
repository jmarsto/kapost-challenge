import sys

import boto3
s3_resource = boto3.resource('s3')

source_bucket_name = sys.argv[1]
destination_bucket_name = sys.argv[2]
threshold = sys.argv[3]

def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)

def copy_objects_over_threshold(source_bucket_name, destination_bucket_name, threshold):
    source_bucket = s3_resource.Bucket(name=source_bucket_name)
    threshold_in_bytes = float(threshold)*1000000
    for obj in source_bucket.objects.all():
        key_name = obj.key
        if (source_bucket.Object(key_name).content_length > threshold_in_bytes):
            copy_to_bucket(source_bucket_name, destination_bucket_name, key_name)

copy_objects_over_threshold(source_bucket_name, destination_bucket_name, threshold)
