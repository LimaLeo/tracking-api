from peewee import *

from src.dao.connect import pg_db


class BaseModel(Model):
    class Meta:
        database = pg_db


class Users(BaseModel):
    id_user = AutoField()
    name = TextField()
    email = CharField(50)
    password = CharField(16)


class Rules(BaseModel):
    id_rule = AutoField()
    name = CharField(30)
    frequency = TimeField()
    description = TextField(null=True)


class MonitoringGroup(BaseModel):
    id_group = AutoField()
    name = CharField(30)
    description = TextField(null=True)
    rule = ForeignKeyField(Rules, backref='groups',
                           on_delete='cascade', on_update='cascade')
    user = ForeignKeyField(Users, backref='groups',
                           on_delete='cascade', on_update='cascade')


class Products(BaseModel):
    id_product = AutoField()
    name = CharField(50)
    link = CharField(100)
    tag = TextField()
    group = ForeignKeyField(
        MonitoringGroup, backref='products', on_delete='cascade', on_update='cascade')


class Prices(BaseModel):
    id_price = AutoField()
    value = DecimalField(6, 2)
    date = DateTimeField(default='Now')
    product = ForeignKeyField(
        Products, backref='prices', on_delete='cascade', on_update='cascade')
