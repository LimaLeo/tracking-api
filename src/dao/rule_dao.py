from peewee import *

from src.model.tracking import Rules
from src.model.tracking import MonitoringGroup
from src.dao.connect import pg_db

def rules_list():
    data = []
    pg_db.connect()
    rules = Rules.select(
        Rules.id_rule,
        Rules.name,
        Rules.description).dicts()
    for row in rules:
        print(row)
        data.append(row)
    pg_db.close()
    return data


def rules_get_monitoring_by_rule(_rule_name):
    data = []
    pg_db.connect()
    monitoringGroup = Rules.select(MonitoringGroup.id_group)\
        .join(MonitoringGroup).where(Rules.name == _rule_name).dicts()
    for row in monitoringGroup:
        data.append(row['id_group'])
    pg_db.close()
    return data
