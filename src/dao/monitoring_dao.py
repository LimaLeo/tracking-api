from peewee import *

from src.model.tracking import MonitoringGroup
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
