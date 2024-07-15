import boto3, os

sns = boto3.client('sns')

def lambda_handler(event,context):
  try:
    response = sns.publish(
      TopicArn= os.environ['SNS_ARN'],
      Message="An image wass uploaded to the S3 bucket"
      )
    print("Message published")
    return response

  except Exception e:
    print(e)
    print("Error publishing message")
    return e
