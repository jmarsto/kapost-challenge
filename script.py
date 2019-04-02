import boto3
s3_resource = boto3.resource('s3')

source_bucket_name = raw_input("Name of Source Bucket: ")
destination_bucket_name = raw_input("Name of Destination Bucket: ")
threshold = float(raw_input("Threshold in MB: "))
source_bucket = s3_resource.Bucket(name=source_bucket_name)

def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)

def copy_objects_over_threshold(source_bucket_name, destination_bucket_name, threshold):
    for obj in source_bucket.objects.all():
        key_name = obj.key
        if (source_bucket.Object(key_name).content_length > float(threshold*1000000)):
            copy_to_bucket(source_bucket_name, destination_bucket_name, key_name)

copy_objects_over_threshold(source_bucket_name, destination_bucket_name, threshold)
