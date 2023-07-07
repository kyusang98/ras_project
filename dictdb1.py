import boto3
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal
import time
from time import sleep
from stock_crawling import dictionary


def write_data(stockname, date, value, dynamodb):
    table = dynamodb.Table('Updown_Values')
    item = {'Updown':updown,
            'Date':date,
            'Value':value}
    table.put_item(Item=item)
    print('item ',updown,' added!')
    print('--------')

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id = "엑세스키",
                          aws_secret_access_key="비밀 엑세스키",
                          region_name = "us-east-2", 
                          #DynamoDB의 리전(region)을 "us-east-2" 미국 동부 (오하이오)로 설정하고 거기에 table을 생성하였으므로
                          #"ap-northeast-2" 아시아 태평양(서울)로 설정하고 코드 돌리면 당연히 table이 없다는 오류가 발생한다.
                          #DynamoDB의 어느 리전에 table을 생성했는지 잘 확인하고 코드 돌려라!
                          endpoint_url = "http://dynamodb.us-east-2.amazonaws.com")


updown = 'updown1'
date = time.strftime('%Y.%m.%d - %H:%M:%S')
value =dictionary
write_data(updown,date,value,dynamodb)
