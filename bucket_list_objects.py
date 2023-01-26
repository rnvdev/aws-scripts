import boto3


s3 = boto3.resource('s3')


for bucket in s3.buckets.all():
    my_bucket = s3.Bucket(bucket.name)
    my_bucket_objects = my_bucket.objects.all()
    list_objects = [file.key for file in my_bucket_objects if file != '']
    result = list_objects if len(list_objects) != 0 else '0 objects.'

    print(f'Inside bucket: {bucket.name}, we have those objects: {result}')