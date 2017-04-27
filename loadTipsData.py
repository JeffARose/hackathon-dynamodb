from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

#dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('tips')

with open("files/tipsdata.json") as json_file:
    tips = json.load(json_file, parse_float = decimal.Decimal)
    for tip in tips:
        tipid = tip['id']
        goal_name = tip['goal_name']
        message = tip['message']

        print("Adding tip:", tipid, goal_name, message)

        table.put_item(
           Item={
               'id': tipid,
               'goal_name': goal_name,
               'message': message
            }
        )
