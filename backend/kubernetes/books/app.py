from flask import Flask, jsonify, make_response,request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import json
import os
import sys
import pymongo


class JSONEncoder(json.JSONEncoder):

    def default(self, json_object: object) -> object:
        if isinstance(json_object, ObjectId):
            return str(json_object)
        return json.JSONEncoder.default(self, json_object)


def db() -> object:
    try:
        uri = os.getenv('MONGO_URI')
        client = pymongo.MongoClient(uri)
        print("Log: Connect successfully\n", client)
        return client
    except Exception as error:
        print("Error connecting to database", error)
        sys.exit(-1)


app = Flask(__name__)
CORS(app)


@app.route("/default", methods=['GET'])
def fill_db() -> object:
    database = db().bookstore
    collection = database['books']
    collection.insert_many(mockData)
    cursor = list(collection.find({}))
    return (
        json.dumps(cursor, cls=JSONEncoder).encode("utf-8"),
        200,
        {'Content-Type':'application/json; charset=utf-8'}
    )


@app.route("/book", methods=['GET'])
def list_books() -> object:
    database = db().bookstore
    collection = database['books']
    cursor = list(collection.find({}))
    return (
        json.dumps(cursor, cls=JSONEncoder).encode("utf-8"),
        200,
        {'Content-Type':'application/json; charset=utf-8'}
    )


@app.route("/book/<id>", methods=['POST'])
def search_book(id: int) -> object:
    database = db().bookstore
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
def status() -> object:
    return make_response(jsonify(msg='OK'), 200)


@app.errorhandler(404)
def resource_not_found(error: object) -> object:
    return make_response(jsonify(error='Not found!'), 404)


def create_app() -> object:
    return app
