import os
from flask import Flask

app = Flask(__name__, static_folder="static", template_folder="templates")

app.config['MONGODB_URI'] = os.environ.get('MONGODB_URI')
app.config['MONGO_URI'] = os.environ.get('MONGODB_URI')
app.config.from_object('api.config')
#app.config.from_envvar('API_CONFIG')

# Import the routes from all controllers
from api.controllers import *