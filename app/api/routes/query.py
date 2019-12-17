from api import app
from flask import request
from flask import render_template
from flask_pymongo import PyMongo

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def index():
    message = request.args.get('m')
    return render_template('index.html', message=message)

@app.route('/template', methods=['GET'])
def template():

    star = mongo.db.stars
    labels = []
    values = []

    for s in star.find():
        labels.append(s['label'])
        values.append(s['value'])

    labels_list = list(map(str, labels))
    values_list = list(map(int, values))

    return render_template('template.html', values=values_list, labels=labels_list)


if __name__ == '__main__':
    app.run(debug=True)