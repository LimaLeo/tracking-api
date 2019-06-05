import json

from src.dao.price_dao import prices_get_price_by_group_id


def get_price_by_group_id(_event, _context):
    queryStringParameters  = _event['queryStringParameters']
    group_id  = queryStringParameters['groupId']
    data  = prices_get_price_by_group_id(group_id)
    response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(data)
        }
    return response
