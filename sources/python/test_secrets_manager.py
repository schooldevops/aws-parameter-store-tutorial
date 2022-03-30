import boto3
import json
import datetime

def convertWithDateTime(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()    
    
# 1. SecretManaget에 접근한다. 
client = boto3.client('secretsmanager')

# # 2. SecretManager를 통해 시크릿을 생성하고, 시크릿을 키/값을 추가한다. 
# response = client.create_secret(
#     Name='my_secret_test_python',
#     SecretString='{"username": "db-name", "password": "db-password"}'
# )

# 임시처리. 
response = client.put_secret_value(
    SecretId='my_secret_test_python',
    SecretString='{"username": "db-name", "password": "db-password"}'
)

# 3. 리스트 목록을 추출한다. 
response = client.list_secrets()

print(response['SecretList'])
for content in response['SecretList']: 
    print('------------------------------')
    print(json.dumps(content, indent=4, default=convertWithDateTime))
    

# 4. retrieve secret value by key

response = client.get_secret_value(
    SecretId='my_secret_test_python'
)

print('--------- retrieve secret value')

database_secrets = json.loads(response['SecretString'])
print(f'username key: {database_secrets.get("username")}')
print(f'password key: {database_secrets.get("password")}')

# 5. 추가적인 시크릿 키/값 등록하기. 
# (주의: 이전에 있던 Secret key/value가 제거된다.)

response = client.put_secret_value(
    SecretId='my_secret_test_python',
    SecretString='{"api_secret": "api_secret_content", "api_access": "api_access_content" }'
)

print(response)

# 6. Update Secrets

response = client.update_secret(
    SecretId='my_secret_test_python',
    Description='Description 내용 수정하기'
)

print(response)

# 7. Delete Secrets
# - RecoveryWindowInDays으로 삭제 대기 시간을 지정한다. 
# - ForceDeleteWithoutRecovery=True를 지정하면 삭제 대기 하지 않는다. 

response = client.delete_secret(
    SecretId='my_secret_test_python',
    RecoveryWindowInDays=10,
    ForceDeleteWithoutRecovery=False
)

# 8. Restore Secret Manager

response = client.restore_secret(
    SecretId='my_secret_test_python'
)

print(response)