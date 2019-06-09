from peewee import *
from datetime import datetime

from src.model.tracking import Prices
from src.model.tracking import Products
from src.model.tracking import MonitoringGroup
from src.dao.connect import pg_db


def insert_one(_value, _product_id):
    prices = Prices(value=_value,
                    product_id=_product_id,
                    )
    return prices.save()


def prices_create(_prices):
    pg_db.connect()
    result = []
    for _ in _prices:
        result.append(insert_one(_["value"], _["product_id"]))
    pg_db.close()
    return result


def prices_get_price_by_group_id(_group_id):
    data = []
    pg_db.connect()
    prices = Prices.select(
            Prices.id_price,
            Prices.date,
            Prices.value,
            Products.id_product,
            Products.link,
            Products.name,
            MonitoringGroup.id_group,
            MonitoringGroup.name,
            MonitoringGroup.description
        )\
        .join(Products).join(MonitoringGroup)\
        .where(Products.group_id == _group_id)\
        .order_by(Prices.date).dicts()
    for row in prices:
        row['date'] = row['date'].strftime("%d/%m/%Y, %H:%M:%S")
        row['value'] = str(row['value'])
        data.append(row)
    pg_db.close()
    return data

