from flask import Flask, jsonify, make_response,request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import json
import os
import sys
import pymongo


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
