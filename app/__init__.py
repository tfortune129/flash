from flask import Flask
from config import Config

# instantiate flask app
app = Flask(__name__)
app.config.from_object(Config)

# establish routes
from . import routes

# this is always the same accross applications