import json

from src.dao.price_dao import prices_create


def create(_event, _context):
    body  = json.loads(_event['body'])
    result  = prices_create(body)
    response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(body)
        }
    return response
