from flask import Flask, redirect, session, Blueprint

# Create a Blueprint for logout routes
logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout', methods=['POST'])  # Allow POST requests for logging out
def logout():
    session.clear()  # Clear the session
    return redirect('/')  # Redirect to home page after logging out
