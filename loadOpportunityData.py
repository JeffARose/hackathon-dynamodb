from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

#dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('opportunitydata')

with open("files/opportunitydata.json") as json_file:
    opps = json.load(json_file, parse_float = decimal.Decimal)
    for opp in opps:
        oppid = opp['id']
        userid = opp['userid']
        acttype = opp['type']
        subject = opp['subject']
        regarding = opp['regarding']

        print("Adding oppdata:", oppid, userid)

        table.put_item(
           Item={
               'id': oppid,
               'userid': userid,
               'type': acttype,
               'subject': subject,
               'regarding': regarding
            }
        )
