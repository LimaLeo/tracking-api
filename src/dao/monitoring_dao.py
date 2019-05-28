from peewee import *

from src.model.tracking import MonitoringGroup
from src.model.tracking import Rules
from src.dao.connect import pg_db


def monitoring_create(_name, _description, _rule_id, _user_id):
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
        MonitoringGroup.rule_id).join(Rules).where(MonitoringGroup.user_id == _user_id).dicts()

    for row in monitoringGroup:
        data.append(row)
    pg_db.close()
    return data

def monitoring_delete(_id_group):
    try:
        pg_db.connect()
        monitoringGroup = MonitoringGroup.get(MonitoringGroup.id_group == _id_group)
        monitoringGroup.delete_instance()
        pg_db.close()
    except(Exception):
        print("produto não encontrado!")

def monitoring_update(_id_group, _name="", _description="", _rule_id="", _user_id=""):
    try:
        pg_db.connect()
        monitoringGroup = MonitoringGroup.get(MonitoringGroup.id_group == _id_group)
        if(_name != ""):
            monitoringGroup.name = _name
        if(_description != ""):
            monitoringGroup.description = _description
        if(_rule_id != ""):
            monitoringGroup.rule_id = _rule_id
        if(_user_id != ""):
            monitoringGroup.user_id = _user_id
        monitoringGroup.save()
        pg_db.close()
    except(Exception):
        print("id não encontrado!")

def monitoring_get_by_id(_id_group):
    data = []
    pg_db.connect()
    monitoringGroup = MonitoringGroup.select().where(MonitoringGroup.id_group == _id_group).dicts()
    for row in monitoringGroup:
        data.append(row)
    pg_db.close()
    return data
