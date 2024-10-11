# routes/home.py
from flask import Blueprint, render_template, redirect, session

# Create a Blueprint for home routes
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    if session.get('username'):
        name = session.get('name')  # Get the name from the session
        return render_template('home.html', name=name)
    else:
        return redirect('/login')
