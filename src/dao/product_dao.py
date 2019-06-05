from peewee import *

from src.model.tracking import Products
from src.model.tracking import MonitoringGroup
from src.dao.connect import pg_db


def product_create(_name, _link, _tag, _group_id):
    pg_db.connect()
    products = Products(name=_name,
                                      link=_link,
                                      tag=_tag,
                                      group_id=_group_id
                                      )
    result = products.save()
    pg_db.close()
    return result

def products_list(_group_id):
    data = []
    pg_db.connect()
    products = Products.select(
        Products.id_product,
        Products.name,
        Products.link,
        Products.tag).where(Products.group_id == _group_id).dicts()
    for row in products:
        data.append(row)
    pg_db.close()
    return data


def products_delete(_id_product):
    try:
        pg_db.connect()
        products = Products.get(Products.id_product == _id_product)
        products.delete_instance()
        pg_db.close()
    except(Exception):
        print("produto não encontrado!")


def products_update(_id_product, _name="", _link="", _tag="", _group_id=""):
    try:
        pg_db.connect()
        products = Products.get(Products.id_product == _id_product)
        if(_name != ""):
            products.name = _name
        if(_link != ""):
            products.link = _link
        if(_tag != ""):
            products.tag = _tag
        if(_group_id != ""):
            products.group_id = _group_id
        products.save()
        pg_db.close()
    except(Exception):
        print("id não encontrado!")

def products_get_by_id(_id_product):
    data = []
    pg_db.connect()
    products = Products.select().where(Products.id_product == _id_product).dicts()
    for row in products:
        data.append(row)
    pg_db.close()
    return data
