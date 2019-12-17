from api import app
from flask import request
from flask import render_template
from flask_pymongo import PyMongo

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def index():
    message = request.args.get('m')
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)