import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):

    try:
        dynamodb.put_item(TableName='devops-kss', Item={'name':{'S':event['name']},'id':{'N':event['id']}})
    except Exception, e:
        print (e)

    return "Done"

        
