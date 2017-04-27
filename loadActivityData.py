from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

#dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('activities')

with open("files/activitydata.json") as json_file:
    activities = json.load(json_file, parse_float = decimal.Decimal)
    for activity in activities:
	id = int(activity['id'])
        targetdate = activity['targetdate']
        userid = int(activity['userid'])
        type = activity['type']
        count = int(activity['count'])
        

        print("Adding activity:", id, targetdate)

        table.put_item(
           Item={
               'id': id,
               'targetdate': targetdate,
               'userid': userid,
               'type': type,
               'count': count
            }
        )

