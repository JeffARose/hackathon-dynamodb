from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

#dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('activitydata')

with open("files/activitydatadata.json") as json_file:
    activities = json.load(json_file, parse_float = decimal.Decimal)
    for activity in activities:
        activity_id = activity['activity_id']
        userid = activity['userid']
        acttype = activity['type']
        subject = activity['subject']
        regarding = activity['regarding']
        start_date = activity['start_date']
        due_date = activity['due_date']
        segment = activity['segment']


        print("Adding activitydata:", activity_id, userid)

        table.put_item(
           Item={
               'activity_id': activity_id,
               'userid': userid,
               'type': acttype,
               'subject': subject,
               'regarding': regarding,
               'start_date': start_date,
               'due_date': due_date,
               'segment': segment
            }
        )
