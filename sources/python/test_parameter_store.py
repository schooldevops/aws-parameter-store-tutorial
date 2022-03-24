# import boto3

# key = '/proejct01/kido/dbname'

# AWS_ACCESS_KEY_ID ="AKslkdfgowhf098290rijsdlkfj6"
# AWS_SECRET_ACCESS_KEY = "myDmmmMMMMMjdgldkfgjldgkjldkgjdlfgE6"
# AWS_DEFAULT_REGION = "ap-northeast-2"
# # ssm = boto3.client('ssm',
# #                       aws_access_key_id=AWS_ACCESS_KEY_ID,
# #                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
# #                       region_name=AWS_DEFAULT_REGION
# #                       )
# ssm = boto3.client('ssm')
# # ssm = boto3.client('ssm')
# parameter = ssm.get_parameter(Name=key, WithDecryption=False)
# print(parameter['Parameter']['Value'])


# import boto3
# from botocore.exceptions import ClientError

# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)
    
# ssm = boto3.client('ssm', 'ap-northeast-2')    
# print(ssm)


# try:
#     param = ssm.get_parameter(Name='/proejct01/kido/dbname', WithDecryption=False)
#     # param = ssm.get_parameters(['/proejct01/kido/dbname', '/proejct01/kido/dbpassword'])
#     print(param['Parameter']['Value'])
# except ClientError as e:
#     if e.response['Error']['Code'] == 'ParameterNotFound':
#         print('Parameter does not exist', e)
#     else:
#         print('parameter exists')


import boto3

DB_NAME = '/project01/myapp/dev/dbname'
DB_PASSWORD = '/project01/myapp/dev/dbpassword'

ssm = boto3.client('ssm')

db_name = ssm.get_parameter(Name=DB_NAME, WithDecryption=False)
db_password = ssm.get_parameter(Name=DB_PASSWORD, WithDecryption=False)

# print(db_name['Parameter']['Value'])
# print(db_password['Parameter']['Value'])

print( f'DB_NAME: {db_name.get("Parameter").get("Value")}' )
print( f'DB_PASSWORD: {db_password.get("Parameter").get("Value")}' )