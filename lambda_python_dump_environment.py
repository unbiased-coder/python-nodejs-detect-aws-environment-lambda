import os

def lambda_handler(event, context):
    for k,v in os.environ.items():
        print (f'{k}={v}')
    
    return

lambda_handler({}, {})