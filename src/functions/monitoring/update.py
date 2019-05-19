import json

from src.dao.monitoring_dao import monitoring_update


def update(_event, _context):
    queryStringParameters  = _event['queryStringParameters']
    group_id  = queryStringParameters['groupId']
    body  = json.loads(_event['body'])
    name  = body['name']
    description = body['description']
    rule_id = body['rule_id']
    user_id = body['user_id']
    result  = monitoring_update(group_id, name, description, rule_id, user_id)
    response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(body)
        }
    return response
