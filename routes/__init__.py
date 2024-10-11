# routes/__init__.py
from flask import Blueprint

# Import each blueprint
from .about import about_bp  # Import the about route
from .contact import contact_bp  # Import the contact route
from .home import home_bp  # Import the home route


# Create a list of blueprints
blueprints = [about_bp,contact_bp,home_bp]  # Add about_bp to the list

def register_routes(app):
    """Register all blueprints to the main app."""
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
