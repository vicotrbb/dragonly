# Encoding UTF-8
# -------------
# .env
# -------------

import sys
from flask import Flask
from .resources import api
import logging
from dotenv import load_dotenv

load_dotenv('.env')

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
app = Flask(__name__, static_folder='static', tamplate_folder='templates')
api.init_app(app)

if __name__ != "__main__":
    logging.info(f"""
    ##########################################
    ####         DRAGONLY API             ####
    ##########################################
    """)


if __name__ == "__main__":
    logging.info(f"""
    ##########################################
    ####         DRAGONLY API             ####
    ##########################################
    """)
    app.run(host="0.0.0.0", port=int("5000"), debug=True, use_reloader=True)
