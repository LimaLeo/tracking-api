import json

from src.dao.product_dao import products_get_by_id


def get_by_id(_event, _context):
    queryStringParameters  = _event['queryStringParameters']
    product_id  = queryStringParameters['productId']
    data  = products_get_by_id(product_id)
    response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(data)
        }
    return response
