from peewee import *

from src.model.tracking import Rules
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
