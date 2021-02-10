# Encoding UTF-8

"""
Elasticsearch provider
----------------------
"""

from elasticsearch import Elasticsearch
from datetime import datetime
import os
import logging

login = os.getenv('ES_LOGIN')
client = os.getenv('ES_CLIENT')

es = Elasticsearch([f"https://{login}@{client}"])


def startup_elasticsearch(app):
    logging.info(f'Initialing Elasticsearch')
    app.elasticsearch = es

# -------------
# QUERY HELPERS
# -------------


def iterator(cursor):
    data = []
    for hits in cursor['hits']['hits']:
        hits['_source']['_id'] = hits['_id']
        data.append(hits['_source'])
    return data


def check_unique(index, data):
    unique = True
    if index != 'user':
        pass
    else:
        for k, v in data.items():
            if k == 'name':
                continue
            doc = {
                "size": 1,
                "query": {
                    "term": {
                        f"{k}.keyword": v
                    }
                }
            }
            res = es.search(index=index,
                            body=doc)
            print(res)
            if res['hits']['total']['value'] > 0:
                raise Exception(
                    f'Fields {k} must be unique')


def check_health():
    try:
        if es.ping():
            return True
        else:
            return False
    except:
        return False
    
def check_unallowed_fields(fields, data):
    if any(field in fields for field in data.keys()):
        raise Exception(
                    f'You are not allowed to change or insert this fields: {fields}')
    

# ---------------
# QUERY FUNCTIONS
# ---------------


def get_document_by_query(index, query, size=10000):
    if query == None or query == '':
        raise Exception('Query must not be empty')
    try:
        res = es.search(index=index,
                        body=query)
    except:
        raise Exception(f'No {index} registered on the base')

    return iterator(res)


def get_all_documents(index, size=10000):
    doc = {
        'size': size,
        'query': {
            'match_all': {}
        }
    }

    try:
        res = es.search(index=index,
                        body=doc)
    except:
        raise Exception(f'No {index} registered on the base')

    return iterator(res)


def get_document(index, id):
    if id == None or id == '':
        raise Exception('Id must not be empty')

    try:
        res = es.get(index=index,
                     id=id)
    except:
        raise Exception(f'{index} not found')

    data = {}
    data['_id'] = res['_id']
    data.update(res['_source'])
    return data


def create_document(index, data):
    check_unique(index, data)
    data['created_at'] = datetime.now()
    data['updated_at'] = datetime.now()

    res = es.index(index=index,
                   body=data)

    if res['result'] == 'created':
        return res['_id']
    else:
        raise Exception(f'An error ocurred when creating the {index}')


def update_document(index, id, data):
    if data == None or not data:
        raise Exception('Empty payload')
    if id == None or id == '':
        raise Exception('Id must not be empty')

    data['updated_at'] = datetime.now()

    try:
        res = es.update(index=index,
                        id=id,
                        body={'doc': data})
    except:
        raise Exception(f'{index} {id} not found')

    return f'{index} {id} updated'


def delete_document(index, id):
    if id == None or id == '':
        raise Exception('Id must not be empty')

    try:
        res = es.delete(index=index,
                        id=id)
    except:
        raise Exception(f'{index} {id} not found')

    return f'{index} {id} deleted'