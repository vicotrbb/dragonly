from flask_restx import fields, Model, marshal
from ... import core

client = core.get_client().notes
note = Model('Note', {
    'note_id': fields.String(required=True, description='The note identifier'),
    'note_path': fields.String(required=True, description='Note markdown path'),
    'note_topics': fields.List(fields.String, required=False, description='Note extracted and created topics'),
    'note_grade': fields.Float(required=False, description='Note generated grade'),
    'date_included': fields.DateTime(required=True, description='Note creation date'),
    'date_changed': fields.DateTime(required=False, description='Note change date'),
    'date_removed': fields.DateTime(required=False, description='Note removal date'),
})


def get_model():
    return note


def get_all_notes():
    res = client.find({})
    return marshal(res, note, skip_none=False)


def get_note(id):
    res = client.find_one({'_id': id})
    return marshal(res, note, skip_none=False)


def find_by_criteria(criteria):
    pass


def create_note(note_dto):
    note_dao = marshal(note_dto, note, skip_none=False)
    res = client.insert_one(note_dao)

    return res.inserted_id is not None


def update_note(id, note_dto):
    note_dao = marshal(note_dto, note, skip_none=True)
    res = client.update_one({'_id': id}, {'$inc': note_dao})

    return res.modified_count > 0


def delete_note(id):
    res = client.delete_one({'_id': id})
    return res.deleted_count > 0
