#-*- coding: utf-8 -*-

from flask import Flask, jsonify, make_response,request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import json
import os
import sys
import pymongo

mockData = {
    "book_id": 1,
    "name": "Leonardo Davinci: La Biografia",
    "image": "https://www.biografiasyvidas.com/biografia/l/fotos/leonardo_da_vinci_2.jpg",
    "author": "Walter Issacson",
    "description":"Basándose en las miles de páginas de los cuadernos manuscritos de Leonardo y nuevos descubrimientos sobre su vida y su obra, Walter Isaacson teje una narración que conecta el arte de Da Vinci con sus investigaciones científicas, y nos muestra cómo el genio del hombre más visionario de la historia nació de habilidades que todos poseemos y podemos estimular, tales como la curiosidad incansable, la observación cuidadosa y la imaginación juguetona. Su creatividad, como la de todo gran innovador, resultó de la intersección entre la tecnología y las humanidades. Despellejó y estudió el rostro de numerosos cadáveres, dibujó los músculos que configuran el movimiento de los labios y pintó la sonrisa más enigmática de la historia, la de la Mona Lisa. Exploró las leyes de la óptica, demostró como la luz incidía en la córnea y logró producir esa ilusión de profundidad en la Última cena.",
    "countInStock": 2,
    "price": 50000
},{
    "book_id": 2,
    "name": "Inteligencia Genial",
    "image": "https://circulocultural.com/wp-content/uploads/2019/03/Inteligencia-Ideal_Tiro.jpg",
    "author": "Michael Gelb",
    "description": "El que, para muchos, ha sido el mayor genio de todos los tiempos, Leonardo da Vinci, puede servir de inspiración a todo aquel que quiera desarrollar al máximo su potencial intelectual y su creatividad. Paso a paso, mediante ejercicios, técnicas y lecciones, este libro muestra el camino para ampliar los horizontes de la mente",
    "countInStock": 3,
    "price": 30000
},{
    "book_id": 3,
    "name": "Metallica: The $24.95 Book",
    "image": "https://images-us.bookshop.org/ingram/9781493061341.jpg?height=500&v=v2",
    "author": "Jo Nesbo",
    "description": "A tense and atmospheric standalone thriller about two brothers, one small town, and a lifetime of dark secrets, from bestselling author Jo Nesbø",
    "countInStock": 5,
    "price": 20000
},{
    "book_id": 4,
    "name": "The Kingdom",
    "image": "https://images-us.bookshop.org/ingram/9780525564867.jpg?height=500&v=v2",
    "author": "Walter Issacson",
    "description":"Basándose en las miles de páginas de los cuadernos manuscritos de Leonardo y nuevos descubrimientos sobre su vida y su obra, Walter Isaacson teje una narración que conecta el arte de Da Vinci con sus investigaciones científicas, y nos muestra cómo el genio del hombre más visionario de la historia nació de habilidades que todos poseemos y podemos estimular, tales como la curiosidad incansable, la observación cuidadosa y la imaginación juguetona. Su creatividad, como la de todo gran innovador, resultó de la intersección entre la tecnología y las humanidades. Despellejó y estudió el rostro de numerosos cadáveres, dibujó los músculos que configuran el movimiento de los labios y pintó la sonrisa más enigmática de la historia, la de la Mona Lisa. Exploró las leyes de la óptica, demostró como la luz incidía en la córnea y logró producir esa ilusión de profundidad en la Última cena.",
    "countInStock": 2,
    "price": 50000
},{
    "book_id": 5,
    "name": "A World Between",
    "image": "https://images-us.bookshop.org/ingram/9781936932955.jpg?height=500&v=v2",
    "author": "Emily Hashimoto",
    "description": "A college fling between two women turns into a lifelong connection--and spells out a new kind of love story for a millennial, immigrant America.",
    "countInStock": 3,
    "price": 30000
},{
    "book_id": 6,
    "name": "The Scythe",
    "image": "https://images-us.bookshop.org/ingram/9780991407309.jpg?height=500&v=v2",
    "author": "Balogun Ojetade",
    "description": "He has been given a second chance at life. A second chance at revenge. He is the bridge between the Quick and the Dead. He is...THE SCYTHE Out of the tragedy of the Tulsa Race Riot of 1921",
    "countInStock": 3,
    "price": 40000
},{
    "book_id": 7,
    "name": "The Inheritance Trilogy",
    "image": "https://images-na.ssl-images-amazon.com/images/I/51mRlKxYZNL._SX342_SY445_QL70_ML2_.jpg",
    "author": "N. K. Jemisin",
    "description": "After her mother's death, a young woman is summoned to the floating city of Sky to claim a royal inheritance she never knew existed in this epic fantasy trilogy from the NYT bestselling author of The Fifth Season.",
    "countInStock": 3,
    "price": 100000
},{
    "book_id": 8,
    "name": "Jonny Appleseed            ",
    "image": "https://images-us.bookshop.org/ingram/9781551527253.jpg?height=500&v=v2",
    "author": "Joshua Whitehead",
    "description": "Jonny Appleseed is a unique, shattering vision of Indigenous life, full of grit, glitter, and dreams.",
    "countInStock": 3,
    "price": 70000
}

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def db():
    # For 'local' testing.
    atlas_uri = os.getenv("mongoUri") 
    if atlas_uri != None:
        client = pymongo.MongoClient(atlas_uri)
        return client

    try:
        uri = f'mongodb://{os.getenv("DOCUMENTDB_USERNAME")}:{os.getenv("DOCUMENTDB_PASSWORD")}@{os.getenv("DOCUMENTDB_HOSTNAME")}:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false'
   
        client = pymongo.MongoClient(uri)
        print("Log: Connect successfully\n", client)
        return client
    except Exception as error:
        print("Error connecting to database", error)
        sys.exit(-1)

app = Flask(__name__)
CORS(app)

@app.route("/default", methods=['GET'])
def fill_db():
    database = db().sample_books
    collection = database['books']
    collection.insert_many(mockData)
    cursor = list(collection.find({}))
    return (
        json.dumps(cursor, cls=JSONEncoder).encode("utf-8"),
        200,
        {'Content-Type':'application/json; charset=utf-8'}
    )

@app.route("/book", methods=['GET'])
def list_books():
    database = db().sample_books
    collection = database['books']
    cursor = list(collection.find({}))
    return (
        json.dumps(cursor, cls=JSONEncoder).encode("utf-8"),
        200,
        {'Content-Type':'application/json; charset=utf-8'}
    )

@app.route("/book/<id>", methods=['POST'])
def search_book(id):
    database = db().sample_books
    collection = database["books"]
    cursor = list(collection.find({"book_id": id}))
    if cursor:
        return (
            json.dumps(cursor, cls=JSONEncoder).encode("utf-8"),
            200,
            {'Content-Type':'application/json; charset=utf-8'}
        )
    else:
        return make_response(jsonify(error='Book not found!'), 404)

@app.route("/book/status", methods=['GET'])
def status():
    return make_response(jsonify(msg='OK'), 200)

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
