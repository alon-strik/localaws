import boto3, boto
import os

s3_client = boto3.client('s3')

lms_bucket = 'lms-releases'
#prefix = 'RC/3.0.1.5/dependencies/bin'
subFolder="VPC-Properties/"
#artifacts=['liquibase','mysql','xml']

#list=s3_client.list_objects(Bucket=lms_bucket,Prefix = subFolder)['Contents']
#
#for s3_key in list:
#    s3_object = s3_key['Key']
#     if not s3_object.endswith("/"):
#        if sum([st in s3_object for st in artifacts]) > 0:
    #print s3_object

#    if  "LMS-VPC-loro-0829141426" in s3_object:
#        print s3_object
#            s3_client.download_file(lms_bucket, s3_object, s3_object)

#     else:
#       if not os.path.exists(s3_object):
#         os.makedirs(s3_object)
#         print 'dir = ' + s3_object


# import boto3
#
s3_client = boto3.client('s3')

bucket = 'lms-releases'


conn = boto. connect_s3(
    # aws_access_key_id=access_key,
    # aws_secret_access_key=secret_key,
    host='objects.dreamhost.com',
    # is_secure=False,               # uncomment if you are not using ssl
    calling_format=boto.s3.connection.OrdinaryCallingFormat(),
)


# prefix = 'RC/3.0.1.5/dependencies/'
#
# # List all objects within a S3 bucket path
#response = s3_client.list_objects(Bucket = s3bucket,Prefix = subFolder)
#
# # # Loop through each file
# for file in response['Contents']:
#
#     # Get the file name
#     name = file['Key'].rsplit('/', 1)
#     print file['Key']
#
#     # Download each file to local disk
#     #s3_client.download_file(bucket, file['Key'], prefix + '/' + name[1])
#     print (file['Key'], name[1])



#
# import boto
# import os
# import boto.s3
# bucket_name = 'lms-releases'
# conn = boto.s3.connect_to_region('eu-west-1')
# bucket = conn.get_bucket(bucket_name)
#
#
# folders = bucket.list("VPC-Properties","/")
# for folder in folders:
#     print folder.name
# # LOCAL_PATH=""
#
# bucket_list = bucket.list()
# for l in bucket_list:
#   keyString = str(l.key)
#   if 'RC/3.0.1.5/dependencies' in keyString:
#         a,b = keyString.split('RC/3.0.1.5/dependencies/')
#         d = LOCAL_PATH + b
#         try:
#             l.get_contents_to_filename(d)
#             print d
#         except OSError:
#             if not os.path.exists(d):
#                 os.mkdir(d)
