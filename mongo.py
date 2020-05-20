from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'Cluster0'
app.config['MONGO_URI'] = 'mongodb+srv://kohler:123@cluster0-qxlqo.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/coutries', methods=['GET'])
def get_all_countries():
    country = mongo.db.country 

    output = []

    for c in country.find():
        output.append({'name' : c['name']})

    return jsonify({'response' : output})

@app.route('/coutries/<name>', methods=['GET'])
def get_one_country(name):
    country = mongo.db.country

    c = country.find_one({'name' : name})

    if c:
        output = {'name' : c['name']}
    else:
        output = 'No results found'

    return jsonify({'response' : output})

@app.route('/coutries', methods=['POST'])
def add_country():
    countries = mongo.db.country 

    name = request.json['name']

    country_id = countries.insert({'name' : name})
    new_country = countries.find_one({'_id' : country_id})

    output = {'name' : new_country['name']}

    return jsonify({'response' : output})

if __name__ == '__main__':
    app.run(debug=True)