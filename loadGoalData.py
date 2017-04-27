from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

#dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('goals')

with open("files/goaldata.json") as json_file:
    goals = json.load(json_file, parse_float = decimal.Decimal)
    for goal in goals:
        goalname = goal['goalname']
        userid = goal['userid']
        target = goal['target']
        actual = goal['actual']

        print("Adding goal:", goalname, userid)

        table.put_item(
           Item={
               'goalname': goalname,
               'userid': userid,
               'target': target,
               'actual': actual
            }
        )
