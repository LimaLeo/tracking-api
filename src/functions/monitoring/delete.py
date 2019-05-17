import json

from src.dao.monitoring_dao import monitoring_delete


def delete(_event, _context):
    queryStringParameters  = _event['queryStringParameters']
    group_id  = queryStringParameters['groupId']
    data  = monitoring_delete(group_id)
    response = {
            "statusCode": 200,
            "body": json.dumps(group_id)
        }
    return response
