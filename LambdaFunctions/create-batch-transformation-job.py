import json
import boto3
from datetime import datetime
import random


client = boto3.client('sagemaker')

def lambda_handler(event, context):
    
    date_today = datetime.today().strftime('%Y-%m-%d')

    year = date_today[0:4]
    month = date_today[5:7]
    day = date_today[8:10]
    
    print(year,month,day)
    
    response = client.create_transform_job(
        TransformJobName = f'{year}-{month}-{day}-object-detection-unique',
        ModelName = 'object-detection-plastic',
        MaxPayloadInMB = 100,
        
        TransformInput = {
            
            'DataSource': {
                'S3DataSource': {
                    'S3DataType': 'S3Prefix',
                    'S3Uri': f's3://plastic-detection-batch-transform-2023/images/{year}/{month}/{day}/'
                }
                
            },
            
            'ContentType' : 'image/jpeg',
            'CompressionType': 'None',
            'SplitType': 'None'
        },
        
        TransformOutput = {
            'S3OutputPath': f's3://plastic-detection-batch-transform-2023/batch-output/{year}/{month}/{day}',
            'AssembleWith': 'None'
        },
        
        TransformResources = {
            'InstanceType': 'ml.m4.xlarge',
            'InstanceCount': 1
        },
        
        DataProcessing = {
            'InputFilter': '$',
            'OutputFilter': '$',
            'JoinSource': 'None'
        }
        
    )
    
    return {
        'body': response
    }