from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

#dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('preferences')

with open("files/prefdata.json") as json_file:
    prefs = json.load(json_file, parse_float = decimal.Decimal)
    for pref in prefs:
        name = pref['name']
        userid = pref['userid']
        pref_value = pref['pref_value']

        print("Adding pref:", name, userid)

        table.put_item(
           Item={
               'name': name,
               'userid': userid,
               'pref_value': pref_value
            }
        )
