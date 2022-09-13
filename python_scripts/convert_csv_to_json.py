import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
import pandas
import csv
import json

s3_client = boto3.client('s3')

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


def lambda_csv_to_json(event, context):
  for record in event['Records']:
      bucket = record['s3']['bucket']['name']
      key = unquote_plus(record['s3']['object']['key'])
      tmpkey = key.replace('/', '')
      download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
      upload_path = '/tmp/fiap-fase3-grupo-l-json-raw'.format(tmpkey)
      s3_client.download_file(bucket, key, download_path)
      csv_to_json(download_path, upload_path)
      s3_client.upload_file(upload_path, '{}-resized'.format(bucket), key)