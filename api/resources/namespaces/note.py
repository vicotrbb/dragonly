from flask_restx import Namespace, Resource
from ..models import note

api = Namespace('Note', description='Notes related operations')
model = note.get_model()
api.add_model('Note', model)


@api.route('/')
@api.route('/<id>')
class Note(Resource):

    @api.doc(responses={200: 'Notes list',
                        404: 'No notes created'})
    @api.marshal_list_with(model)
    def get(self):
        '''List all notes'''
        return []

    @api.doc('create_note')
    @api.expect(model)
    def post(self):
        '''Create a new note'''
        pass


@api.route('/<id>')
@api.param('id', 'The note identifier')
@api.response(404, 'Note not found')
class NoteId(Resource):

    @api.doc('put_note')
    @api.marshal_with(model)
    def put(self, id):
        '''Updates a note given its identifier'''
        pass

    @api.doc('delete_note')
    @api.marshal_with(model)
    def delete(self, id):
        '''Delete a note given its identifier'''
        pass

    @api.doc('get_id_note')
    @api.marshal_with(model)
    def get(self, id):
        '''Fetch a note given its identifier'''
        pass
