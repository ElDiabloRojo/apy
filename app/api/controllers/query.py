from api import app
from flask import request
from flask import render_template
from flask_pymongo import PyMongo

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def index():
    message = request.args.get('m')
    return render_template('index.html', message=message)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)