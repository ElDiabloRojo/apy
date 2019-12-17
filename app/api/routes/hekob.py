from api import app
import logging
from flask_pymongo import PyMongo
from flask import Flask
from flask import Markup
from flask import render_template

mongo = PyMongo(app)

star = mongo.db.stars
labels = []
values = []

for s in star.find():
    labels.append(s['label'])
    values.append(s['value'])

labels_list = list(map(str, labels))
values_list = list(map(int, values))

@app.route('/bar')
def bar():
    bar_labels = labels_list
    bar_values = values_list
    return render_template('bar_chart.html', title='apy', max=max(values_list), labels=bar_labels, values=bar_values)

@app.route('/line')
def line():
    line_labels = labels_list
    line_values = values_list
    return render_template('line_chart.html', title='apy', max=max(values_list), labels=line_labels, values=line_values)

@app.route('/pie')
def pie():
    pie_labels = labels_list
    pie_values = values_list
    return render_template('pie_chart.html', title='apy', max=max(values_list), set=zip(pie_values, pie_labels, colors))

if __name__ == '__main__':
    app.run(debug=True)