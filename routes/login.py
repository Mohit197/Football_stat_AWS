from flask import Flask, render_template, request, redirect, session, make_response, jsonify, url_for, Blueprint
from db import db  # Import the db object directly
import bcrypt

# Create a Blueprint for login routes
login_bp = Blueprint('login', __name__)
@login_bp.route('/login', methods=['GET', 'POST'])  # Allow both GET and POST methods
def login():
    if request.method == 'POST':
        users = db.users
        login_user = users.find_one({'username': request.form['username']})  # Change key to 'username'

        if login_user and bcrypt.checkpw(request.form['password'].encode('utf-8'), login_user['password']):
            session['username'] = request.form['username']
            session['name'] = login_user['name']  # Store the user's name in the session
            session['age'] = login_user['age']  # Store the user's age in the session
            return jsonify({'redirect': '/'})  # Redirect to home page
        else:
            return jsonify({'error': 'Invalid username/password combination'}), 400  # Return error with status code 400
    else:
        # Handle GET request
        return render_template('login.html')  # Render the login page for GET requests