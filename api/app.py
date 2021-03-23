# Encoding UTF-8
# -------------
# .env
# -------------

import sys
from flask import Flask
import resources
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
app = Flask(__name__)
resources.api.init_app(app)

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
    app.run(host="0.0.0.0", port=int("5000"), debug=True, use_reloader=True, load_dotenv='.env')
