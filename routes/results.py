from flask import Blueprint, session, redirect, render_template

results_bp = Blueprint('results', __name__)

@results_bp.route("/results")
def results():
    # Check if the user is logged in
    if 'name' not in session:
        return redirect('/login')
    
    # Check if the quiz is completed
    if 'quiz_completed' in session:
        return render_template('results.html')
    else:
        return redirect('/questions')
