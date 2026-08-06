import json
import boto3
import uuid

s3 = boto3.client('s3')
BUCKET_NAME = 'student_pdf_uploader'

def lambda_handler(event, context):
    file_name = json.loads(event['body'])['fileName']
    file_key = f"{uuid.uuid4()}-{file_name}"

    presigned_url = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={
            'Bucket': student_pdf_uploader,
            'Key': file_key,
            'ContentType': 'application/pdf'
        },
        ExpiresIn=300  # URL valid for 5 minutes
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'uploadUrl': presigned_url,
            'key': file_key
        })
    }
