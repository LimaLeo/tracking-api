import json

from src.dao.rule_dao import rules_get_monitoring_by_rule


def get_monitoring_by_rule(_event, _context):
    queryStringParameters  = _event['queryStringParameters']
    ruleName  = queryStringParameters['ruleName']
    groups = rules_get_monitoring_by_rule(ruleName)
    response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(groups)
        }
    return response
