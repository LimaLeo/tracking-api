from peewee import *

from src.model.tracking import MonitoringGroup
from src.model.tracking import Rules
from src.dao.connect import pg_db


def create_monitoring(_name, _description, _rule_id, _user_id):
    pg_db.connect()
    monitoringGroup = MonitoringGroup(name=_name,
                                      description=_description,
                                      rule_id=_rule_id,
                                      user_id=_user_id
                                      )
    result = monitoringGroup.save()
    pg_db.close()
    return result

def monitoring_list(_user_id):
    data = []
    pg_db.connect()
    monitoringGroup = MonitoringGroup.select(
        MonitoringGroup.name,
        MonitoringGroup.description,
        Rules.description.alias('rule')).join(Rules).dicts()
    for row in monitoringGroup:
        data.append(row)
    pg_db.close()
    return data

def monitoring_delete(id_group):
    try:
        pg_db.connect()
        monitoringGroup = MonitoringGroup.get(MonitoringGroup.id_group == id_group)
        monitoringGroup.delete_instance()
        pg_db.close()
    except(Exception):
        print("produto não encontrado!")
