from flask_restx import fields, Model

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
    pass

def get_note(id):
    pass

def create_note():
    pass

def update_note(id):
    pass

def delete_note(id):
    pass