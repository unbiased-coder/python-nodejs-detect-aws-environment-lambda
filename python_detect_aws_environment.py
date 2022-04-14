import os

def is_aws_env():
    return os.environ.get('AWS_LAMBDA_FUNCTION_NAME') or os.environ.get('AWS_EXECUTION_ENV')
    
def lambda_handler(event, context):
    if is_aws_env():
        print ('We are running inside an AWS environment')
    else:
        print ('We are running outside an AWS environment')

if not is_aws_env():
    lambda_handler({}, {})
