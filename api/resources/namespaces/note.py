from flask_restx import Namespace, Resource
from ..models import note

api = Namespace('Note', description='Notes related operations')
api.add_model('Note', note)


@api.route('/')
class Note(Resource):

    @api.doc(responses={200: 'Notes list',
                        404: 'No notes created'})
    @api.marshal_list_with(note)
    def get(self):
        '''List all notes'''
        return []

    @api.doc('create_note')
    @api.expect(note)
    def post(self):
        '''Create a new note'''
        pass


@api.route('/<id>')
@api.param('id', 'The note identifier')
@api.response(404, 'Note not found')
class NoteId(Resource):

    @api.doc('get_note')
    @api.marshal_with(note)
    def get(self, id):
        '''Fetch a note given its identifier'''
        pass

    @api.doc('put_note')
    @api.marshal_with(note)
    def put(self, id):
        '''Updates a note given its identifier'''
        pass

    @api.doc('delete_note')
    @api.marshal_with(note)
    def delete(self, id):
        '''Delete a note given its identifier'''
        pass
