from __future__ import print_function # Python 2/3 compatibility
import boto3
import sys

#dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table(sys.argv[1])

table.delete()
