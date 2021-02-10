# Encoding UTF-8
"""
Api routing
"""

from flask_restx import Namespace

def initialize_routes(api):
    note = Namespace('Note', description='Notes related endpoints', path='/note')
    
    # Notes routes
    note.add_resource("///////", '')
    note.add_resource("///////", '/<id>')
    api.add_namespace(note)
