from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

#dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('userinfo')

with open("files/userinfodata.json") as json_file:
    userinfo = json.load(json_file, parse_float = decimal.Decimal)
    for user in userinfo:
	userid = int(user['userid'])
	last_name  = user['last_name']
	first_name  = user['first_name']
	account_type  = user['account_type']
        address1 = user['address1']
        city = user['city']
        state = user['state']
        zip = user['zip']

        print("Adding user:", userid)

        table.put_item(
           Item={
               'userid': userid,
               'last_name': last_name,
               'first_name': first_name,
               'account_type': account_type,
               'fr_number': "12345",
               'address1': address1,
               'city': city,
               'state': state,
               'zip': zip
            }
        )

