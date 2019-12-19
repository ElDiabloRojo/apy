from api import app
from flask import render_template
from flask_pymongo import PyMongo

mongo = PyMongo(app)

@app.route('/chart', methods=['GET'])
def chart():

    star = mongo.db.stars
    labels = []
    durations = []
    values = []

    for s in star.find():
        labels.append(s['label'])
        durations.append(s['duration'])
        values.append(s['value'])

    labels_list = list(map(str, labels))
    durations_list = list(map(int, durations))
    values_list = list(map(int, values))

    return render_template('chart.html', values=values_list, durations=durations_list, labels=labels_list)


if __name__ == '__main__':
    app.run(debug=True)