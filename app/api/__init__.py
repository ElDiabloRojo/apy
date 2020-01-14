import os
from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__, static_folder="static", template_folder="templates")

app.config['MONGODB_URI'] = os.environ.get('MONGODB_URI') + "?retryWrites=false"
app.config['MONGO_URI'] = os.environ.get('MONGODB_URI') + "?retryWrites=false"
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
app.config.from_object('api.config')
#app.config.from_envvar('API_CONFIG')

# Import the routes from all controllers
from api.controllers import *