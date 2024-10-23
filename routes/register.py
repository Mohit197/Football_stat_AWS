from flask import Flask, render_template, request, redirect, session, make_response, jsonify, url_for, Blueprint
from db import db  # Import the db object directly
import bcrypt

# Create a Blueprint for register routes
register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])  # Allow both GET and POST methods
def register():
    if request.method == 'POST':
        users = db.users
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            # Hash the password
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            # Insert user details into the database
            users.insert_one({
                "username": request.form['username'],
                "name": request.form['name'],
                "age": int(request.form['age']),
                'password': hashpass
            })
            return redirect("/login")  # Redirect to login after successful registration
        return "That username already exists!"
    return render_template('register.html')
