from peewee import *

from src.model.tracking import Prices
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


