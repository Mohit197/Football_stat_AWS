# user_routes.py
from flask import Blueprint, render_template, redirect, session, url_for

# Create a Blueprint for user routes
user_bp = Blueprint('user', __name__)

@user_bp.route("/user")
def user():
    # Check if the user is logged in
    if 'name' not in session:
        return redirect('/login')

    user_info = {
        'name': session.get('name'),
        'image_url': url_for('static', filename='images/Football_Background3.jpg'),  # Removed the leading slash
        'age': session.get('age')
    }
    return render_template('user.html', user_info=user_info)

@user_bp.route("/user-home")
def userhome():
    return render_template('user-home.html')

@user_bp.route("/user-about")
def userabout():
    return render_template('user-about.html')
