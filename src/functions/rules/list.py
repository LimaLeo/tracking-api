import json

from src.dao.rule_dao import rules_list


def _list(_event, _context):
    data  = rules_list()
    response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(data)
        }
    return response
