# routes/contact.py
from flask import Blueprint, render_template

# Create a Blueprint for contact routes
contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact')
def contact():
    return render_template('contact.html')
