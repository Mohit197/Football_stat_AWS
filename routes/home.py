from flask import Blueprint, render_template, redirect, session, make_response

# Create a Blueprint for home routes
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    if 'username' in session:
        name = session.get('name')  # Get the name from the session
        response = make_response(render_template('home.html', name=name))
        
        # Set cache-control headers
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        
        return response
    else:
        return redirect('/login')
