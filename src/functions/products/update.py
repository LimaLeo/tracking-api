import json

from src.dao.product_dao import products_update


def update(_event, _context):
    queryStringParameters  = _event['queryStringParameters']
    product_id  = queryStringParameters['productId']
    body  = json.loads(_event['body'])
    name  = body['name']
    link = body['link']
    tag = body['tag']
    group_id = body['group_id']
    result  = products_update(product_id, name, link, tag, group_id)
    response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(body)
        }
    return response
