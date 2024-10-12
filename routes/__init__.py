# routes/__init__.py
from flask import Blueprint

# Import each blueprint
from .about import about_bp  
from .contact import contact_bp  
from .home import home_bp  
from .register import register_bp  
from .login import login_bp  
from .logout import logout_bp 
from .user import user_bp
from .quiz_route import quiz_bp
from .results import results_bp
from .password_reset import password_reset_bp


# Create a list of blueprints
blueprints = [about_bp,contact_bp,home_bp,register_bp,login_bp,logout_bp,user_bp,quiz_bp,results_bp,password_reset_bp]  # Add about_bp to the list

def register_routes(app):
    """Register all blueprints to the main app."""
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
