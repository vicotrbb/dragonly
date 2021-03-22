from flask_restx import Api
import os
from .namespaces import note

api = Api(
    title='Dragonly',
    version='1.0',
    description='A description'
)

api.add_namespace(note, path='/api/notes')