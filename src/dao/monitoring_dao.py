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
        MonitoringGroup.id_group,
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

def monitoring_update(id_group, name="", description="", rule_id="", user_id=""):
    try:
        pg_db.connect()
        monitoringGroup = MonitoringGroup.get(MonitoringGroup.id_group == id_group)
        if(name != ""):
            monitoringGroup.name = name
        if(description != ""):
            monitoringGroup.description = description
        if(rule_id != ""):
            monitoringGroup.rule_id = rule_id
        if(user_id != ""):
            monitoringGroup.user_id = user_id
        monitoringGroup.save()
        pg_db.close()
    except(Exception):
        print("id não encontrado!")

def monitoring_get_by_id(id_group):
    data = []
    pg_db.connect()
    monitoringGroup = MonitoringGroup.select().where(MonitoringGroup.id_group == id_group).dicts()
    for row in monitoringGroup:
        data.append(row)
    pg_db.close()
    return data
