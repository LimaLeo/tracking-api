import json

from src.dao.product_dao import product_create


def create(_event, _context):
    body  = json.loads(_event['body'])
    name  = body['name']
    link = body['link']
    tag = body['tag']
    group_id = body['group_id']
    result  = product_create(name, link, tag, group_id)
    response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(body)
        }
    return response
