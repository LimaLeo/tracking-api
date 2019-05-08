import json

from src.dao.monitoring_dao import create_monitoring


def create(_event, _context):
    body  = json.loads(_event['body'])
    name  = body['name']
    description = body['description']
    rule_id = body['rule_id']
    user_id = body['user_id']
    result  = create_monitoring(name, description, rule_id, user_id)
    response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    return response
