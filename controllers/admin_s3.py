import boto3
from keys import ACCESS_KEY, SECRET_KEY

bucket_name = 'bucket-cym-290-w'
def connection_s3():
    session_aws = boto3.session.Session(ACCESS_KEY, SECRET_KEY)
    session_s3 = session_aws.resource('s3')
    return session_s3

def get_objects_s3():
    session_s3 = connection_s3()
    bucket_conn = session_s3.Bucket(bucket_name)
    bucket_objects = bucket_conn.objects.all()
    for obj in bucket_objects:
        print(obj.key)

def upload_file_s3(image, id):
    session_s3 = connection_s3()
    extension = image.filename.split(".")[1]
    image_path_local = "/tmp/" + id + "." + extension
    image.save(image_path_local)
    image_path_destination = "images/" + id + "." + extension
    session_s3.meta.client.upload_file(image_path_local, bucket_name, image_path_destination)
    print("Photo uploaded to s3")
