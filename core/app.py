# Encoding UTF-8
# -------------
# .env
# -------------

from dotenv import load_dotenv
load_dotenv('.env')

import logging
from resources import cache, api, es_provider
from start import routes
from flask import Flask
from flask_restx import Api
import sys

# -------------
# Api startup
# -------------

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
app = Flask(__name__, static_folder='static', tamplate_folder='templates')

api.startup_api(app)
routes.initialize_routes(api.api)

if __name__ != "__main__":
    logging.info(f'Initializing app')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True, use_reloader=True)