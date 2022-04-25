import json
import string
import random
import boto3


s3_client = boto3.client('s3')
# accessing s3 bucket 
s3 = boto3.resource('s3')
bucket = s3.Bucket('greensocksapp')

# accessing dynamo 
client = boto3.resource('dynamodb')
# accessing table within dynamo
table = client.Table('greensocksdata')





def loadData(event, context):
    # print(f"got the event {event}")
    try:
        
        exp_id = event["queryStringParameters"]['exp_id']
        key = exp_id + '.json'
        print(f"key is......{key} ")

        s3_clientobj = s3_client.get_object(Bucket='greensocksapp', Key= key) # declare globally 
        s3_clientdata = s3_clientobj['Body'].read().decode('utf-8')
        s_load = json.loads(s3_clientdata)
        
    except Exception as e:
        print(e)
        
    response = {
        "statusCode": 200,
        "headers": {'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': True,
                   },
        "body": json.dumps({
                            'event' : s_load
                            })
    }
    return response





def saveData(event, context):
    print(f"got the event")
    try:
        event = json.loads(event['body'])
        p_id = event['objects'][0]['p_id']
        submit_time = event['objects'][1]['time']
        experiment_id = event['objects'][2]['exp_id']
        left_index = event['objects'][3]['left_index']
        right_index = event['objects'][4]['right_index']
        choice = event['objects'][5]['choice']

        # print(f"inside try {json.dumps(event)}")
        
        id1 = ''.join(random.choice(string.ascii_uppercase) for i in range(10))
        bucket.put_object(Key='{}.json'.format(id1),
                        Body=json.dumps(event),
                        ACL='public-read', 
                        ContentType='application/json')
        
        
        print(f"getting table status{table.table_status}")

        # putting items into greensocksdata table 
        table.put_item(Item= {'p_id' : str(p_id),
                              'submit_time': str(submit_time),
                              'experiment_id': str(experiment_id),                                
                              'left_index': str(left_index),
                              'right_index' : str(right_index),
                              'choice': str(choice)
                               })
        
    except Exception as e:
        print(e)
        
    response = {
        "statusCode": 200,
        "headers": {'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': True,
                   },
        "body": json.dumps({'message':'SUCCESS2',
                            'event' : event
                            })
    }
    return response
