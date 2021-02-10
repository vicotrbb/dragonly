# Encoding UTF-8

from flask_restx import Api
import logging

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-auth'
    }
}

api = Api(authorizations=authorizations)

def startup_api(app):
    logging.info(f'Initializing Api')
    api.init_app(app,
                 version='0.1.0',
                 title='Dragonly backend',
                 )
