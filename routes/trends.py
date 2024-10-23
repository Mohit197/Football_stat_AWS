from flask import Blueprint, render_template, request, redirect, url_for, session, make_response
from datetime import datetime
from db import db
from pymongo import MongoClient
from bson.objectid import ObjectId

# Setup Blueprint for modular routing
trends_bp = Blueprint('trends', __name__)

# Route to create a new trend
@trends_bp.route('/create_trend', methods=['POST'])
def create_trend():
    if 'username' in session:
        trend_content = request.form['trend_content']
        db.trends.insert_one({
            'username': session['username'],
            'content': trend_content,
            'timestamp': datetime.utcnow()
        })
        return redirect(url_for('trends.view_trends'))
    return redirect("/login")

# Route to edit an existing trend (only user's own trend)
@trends_bp.route('/edit_trend/<trend_id>', methods=['POST'])
def edit_trend(trend_id):
    if 'username' not in session:
        return redirect("/login")

    trend = db.trends.find_one({'_id': ObjectId(trend_id)})

    # Ensure the user can only edit their own trends
    if trend and trend['username'] == session['username']:
        new_content = request.form['new_content']
        db.trends.update_one({'_id': ObjectId(trend_id)}, {'$set': {'content': new_content}})
    
    return redirect(url_for('trends.view_trends'))

# Route to view all trends
@trends_bp.route('/trends')
def view_trends():
    # Check if the user is logged in
    if 'username' not in session:
        return redirect("/login")
    
    # Fetch all trends from the database
    trends = db.trends.find().sort('timestamp', -1)
    
    # Format the timestamp for each trend before sending to template
    formatted_trends = []
    for trend in trends:
        trend['formatted_timestamp'] = trend['timestamp'].strftime('%Y-%m-%d %H:%M')
        formatted_trends.append(trend)

    # Create response and set cache control headers
    response = make_response(render_template('trends.html', trends=formatted_trends))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response
