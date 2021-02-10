# Encoding UTF-8
# Project schemas

from . import api
from flask_restx import fields

api = api.api

note = api.model('Note', {
    '_id': fields.String(required=True, description='Document id', example='yfojRnQBJiSI16yB9fcn'),
})
