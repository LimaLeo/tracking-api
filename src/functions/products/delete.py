import json

from src.dao.product_dao import products_delete


def delete(_event, _context):
    queryStringParameters  = _event['queryStringParameters']
    product_id  = queryStringParameters['productId']
    data  = products_delete(product_id)
    response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(product_id)
        }
    return response
