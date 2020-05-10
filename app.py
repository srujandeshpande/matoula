import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
from io import StringIO
import base64
import requests
import random
from datetime import date

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'\xd2(*K\xa0\xa8\x13]g\x1e9\x88\x10\xb0\xe0\xcc'

#Loads the Database and Collections
mongo = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0-idj9s.gcp.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
db = pymongo.database.Database(mongo, 'matoula1')


@app.route('/')
def root_test():
    return render_template("login.html")

@app.route('/new_user', methods=['GET'])
def new_user():
    return render_template("new_user.html")


@app.route('/tests/build_test')
def build_test():
    return "Passed"

#Login
@app.route('/api/login', methods=['POST'])
def applogin():
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.json
    for i in json.loads(dumps(User_Data.find())):
        if i['_id'] == inputData['email'] and i['password'] == inputData['password']:
            return Response(status=200)
    return Response(status=403)

@app.route('/login', methods=['POST'])
def weblogin():
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.form
    for i in json.loads(dumps(User_Data.find())):
        if i['_id'] == inputData['email'] and i['password'] == inputData['password']:
            session['email'] = i['_id']
            return render_template("dashboard.html")
    return Response(status=403)

#Create New User
@app.route('/api/new_user', methods=['POST'])
def appnew_user():
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.json
    for i in json.loads(dumps(User_Data.find())):
        if i['_id'] == inputData['email']:
            return Response(status=403)
        else:
            User_Data.insert_one({"_id":inputData["email"],"password":inputData["password"],"count":0})
            return Response(status=200)

@app.route('/add_new_user', methods=['POST'])
def add_new_user():
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.form
    User_Data.insert_one({"_id":inputData["email"],"password":inputData["password"],"count":0})
    return render_template("login.html")
    '''
    for i in json.loads(dumps(User_Data.find())):
        if i['_id'] == inputData['email']:
            return Response(status=403)
        else:
            User_Data.insert_one({"_id":inputData["email"],"password":inputData["password"],"count":0})
            return render_template("login.html")
    '''
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
@app.route('/add_new_item', methods=['POST'])
def add_new_item():
    Item_Data = pymongo.collection.Collection(db, 'Item_Data')
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.form
    for i in json.loads(dumps(User_Data.find())):
        if i['_id'] == session['email']:
            newcount = int(i['count'])+1
            #print(inputData['worntoday'])
            if inputData['worntoday'] == 'on':
                today = date.today()
                worntoday = today.strftime("%d %B %Y")
            else:
                worntoday = "Never"
            #print(str(inputData['worntoday']))
            #date = "Never"
            User_Data.update_one({"_id":session["email"]},{'$set':{"count":newcount}})
            Item_Data.insert_one({"email":i['_id'], "index":newcount, "name":inputData["name"], "type":inputData["type"], "color":inputData["color"], "lastworn":worntoday})
            return render_template("dashboard.html")
    return Response(status=403)