from flask import Blueprint, render_template

password_reset_bp = Blueprint('password_reset', __name__)

@password_reset_bp.route('/password_reset')
def password_reset():
    # This will render the password reset form where users input their email
    return render_template('password_reset.html')
