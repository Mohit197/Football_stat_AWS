# routes/about.py
from flask import Blueprint, render_template, redirect, session

# Create a Blueprint for about routes
about_bp = Blueprint('about', __name__)

@about_bp.route('/about')
def about():
    # Check if the user is logged in
    if 'name' not in session:
        return redirect('/login')
    return render_template('about.html')
