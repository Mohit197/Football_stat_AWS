from flask import Flask, render_template, request, redirect, session, jsonify, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
import bcrypt
from db import db  # Database connection
from routes import register_routes  # Register routes

app = Flask(__name__)
app.secret_key = "12ax12221zzx57z"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Register all routes
register_routes(app)


#Not Sure When This Belong, SO For now leave it here
@app.route('/check_user_exists')
def check_user_exists():
    username = request.args.get('username')
    users = db.users
    existing_user = users.find_one({'name': username})
    return jsonify({'exists': existing_user is not None})


## How Activate Virtual Enivorment"
#source venv/bin/activate 