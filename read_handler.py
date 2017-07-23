import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):

    try:
        result = dynamodb.get_item(TableName='devops-kss', Key={'name':{'S':event['name']}})
    except Exception, e:
        print (e)

    return result['Item']

        
