"""
    The code in this file connects the model and the view.
"""

from model.model import Motorcycle, Base, Client, BaseMotorcycle
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///model/ms.db", echo=True)
# Session = sessionmaker(bind=engine)
Session = sessionmaker(
    binds={
        Base: engine,
    },
    expire_on_commit=False,
)
session = Session()
"""
    Add a new item to the Item table. Data must be in a dictionary.
"""


def add_motorcycle(data):
    moto = Motorcycle()
    moto.name = data['name']
    moto.document = data['document']
    session.add(moto)
    session.commit()
    session.close()


def add_client(data):
    client = Client()
    client.name = data['name']
    client.motorcycle_id = data['motorcycle_id']
    # client.motorcycle = data['motorcycle']
    session.add(client)
    session.commit()
    session.close()


#
# """
#     Get everything from tables Item and Category and create a list of ItemObj
# """
# def get_items():
#     items = session.query(Item).all()
#     cats = session.query(Category).all()
#     itemObjs = []
#     for item in items:
#         cat = [c for c in cats if c.id == item.cat_id][0]
#         itemObj = ItemObj(item, cat)
#         itemObjs.append(itemObj)
#     session.close()
#     return itemObjs


def get_motorcycles():
    motorcycles = session.query(Motorcycle).all()
    session.close()
    return motorcycles


def get_base_motorcycles():
    motorcycles = session.query(BaseMotorcycle).all()
    if motorcycles is None:
        raise ValueError("Сокровище не найдено!")
    session.close()
    return motorcycles


def get_clients():
    clients = session.query(Client).all()
    session.close()
    return clients


def get_motorcycle(document):
    stmt = (select(Motorcycle).where(Motorcycle.document == document))
    motorcycle = session.scalars(stmt).one()
    if motorcycle is None:
        raise ValueError("Сокровище не найдено!")
    session.close()
    return motorcycle.id
