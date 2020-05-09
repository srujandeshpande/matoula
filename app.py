import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
from io import StringIO
import base64
import requests
import random

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'\xd2(*K\xa0\xa8\x13]g\x1e9\x88\x10\xb0\xe0\xcc'

#Loads the Database and Collections
mongo = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0-idj9s.gcp.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
db = pymongo.database.Database(mongo, 'matoula1')


@app.route('/')
def root_test():
	return "Welcome to Matoula!"

@app.route('/tests/build_test')
def build_test():
	return "Passed"

#Login
@app.route('/api/login', methods=['POST'])
def login():
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.json
    for i in json.loads(dumps(User_Data.find())):
        if i['_id'] == inputData['email'] and i['password'] == inputData['password']:
            return Response(status=200)
    return Response(status=403)

#Create New User
@app.route('/api/new_user', methods=['POST'])
def new_user():
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.json
    for i in json.loads(dumps(User_Data.find())):
        if i['_id'] == inputData['email']:
            return Response(status=403)
        else:
            User_Data.insert_one({"_id":inputData["email"],"password":inputData["password"],"count":0})
            return Response(status=200)

#Forgot Password
@app.route('/api/forgot_password', methods=['POST'])
def forgot_password():
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.json
    for i in json.loads(dumps(User_Data.find())):
        if i['_id'] == inputData['email']:
            return (str(i['password']))
    return Response(status=403)


#Add new clothing
@app.route('/api/add_new_item', methods=['POST'])
def add_new_item():
    Item_Data = pymongo.collection.Collection(db, 'Item_Data')
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.json
    for i in json.loads(dumps(User_Data.find())):
        if i['_id'] == inputData['email']:
            newcount = int(i['count'])+1
            User_Data.update_one({"_id":inputData["email"]},{"count":newcount})
            Item_Data.insert_one({"email":i['_id'], "index":newcount, "name":inputData["name"], "type":inputData["type"], "color":inputData["color"], "addedDate":inputData["dateTime"], "image":inputData["image"]})
            return Response(status=200)
    return Response(status=403)
