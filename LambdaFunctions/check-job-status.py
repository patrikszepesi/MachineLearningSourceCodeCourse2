import json
import boto3
from datetime import datetime


client = boto3.client('sagemaker') 

date_today = datetime.today().strftime('%Y-%m-%d')

year = date_today[0:4]
month = date_today[5:7]
day = date_today[8:10]



def lambda_handler(event, context):
    
    try:
       
       name = f'{year}-{month}-{day}-object-detection-unique'
       
       response = client.describe_transform_job(TransformJobName = name)
       
       jobStatus = response['TransformJobStatus']
        
       return jobStatus #Failed, Completed, InProgress
       
       
    except Exception as e:
        print(e)
        message = 'Error getting Batch Job status'
        print(message)
        raise Exception(message)
