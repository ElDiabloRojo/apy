from api import app
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

mongo = PyMongo(app)

@app.route('/star', methods=['GET'])
def get_all_stars():
    star = mongo.db.stars
    output = []
    for s in star.find():
        output.append({'label' : s['label'], 'value' : s['value']})
    return jsonify({'result' : output})

@app.route('/star/', methods=['GET'])
def get_one_star(label):
    star = mongo.db.stars
    s = star.find_one({'label' : label})
    if s:
        output = {'label' : s['label'], 'value' : s['value']}
    else:
        output = "No such name"
    return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():
    star = mongo.db.stars
    label = request.json['label']
    value = request.json['value']
    star_id = star.insert({'label': label, 'value': value})
    new_star = star.find_one({'_id': star_id })
    output = {'label' : new_star['label'], 'value' : new_star['value']}
    return jsonify({'result' : output})

@app.route('/purge', methods=['POST'])
def purge():
    star = mongo.db.stars
    query = request.args.get('d')
    if query == 'true':
        purge_stars = star.delete_many({})
    return jsonify({'result' : purge_stars.deleted_count})

if __name__ == '__main__':
    app.run(debug=True)
