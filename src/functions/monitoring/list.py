import json

from src.dao.monitoring_dao import monitoring_list


def _list(_event, _context):
    queryStringParameters  = _event['queryStringParameters']
    user_id  = queryStringParameters['userId']
    data  = monitoring_list(user_id)
    response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
    return response
