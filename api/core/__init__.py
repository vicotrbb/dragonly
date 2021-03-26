from .mongo_connector import db


def get_client():
    return db
