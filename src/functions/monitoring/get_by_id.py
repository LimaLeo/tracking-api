import json

from src.dao.monitoring_dao import monitoring_get_by_id


def get_by_id(_event, _context):
    queryStringParameters  = _event['queryStringParameters']
    group_id  = queryStringParameters['groupId']
    data  = monitoring_get_by_id(group_id)
    response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(data)
        }
    return response
