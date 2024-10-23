from flask import Blueprint, render_template, request, redirect, session
from db import db  # Import the database connection


quiz_bp = Blueprint('quiz', __name__)


def read_questions_from_file(file_path):
    questions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_question = None
        
        for line in lines:
            line = line.strip()
            if line.startswith("Q"):
                if current_question:
                    questions.append(current_question)
                current_question = {"text": "", "choices": []}
                question_parts = line.split(':', 1)
                if len(question_parts) == 2:
                    current_question["text"] = question_parts[1].strip()
            else:
                if current_question is not None:
                    current_question["choices"].append(line.strip())
        
        if current_question:
            questions.append(current_question)
    
    return questions

questions = read_questions_from_file('questions.txt')

@quiz_bp.route("/questions", methods=['GET', 'POST'])
def question():
    # Check if the user is logged in
    if 'name' not in session:
        return redirect('/login')
    
    # Check if the quiz is completed
    if 'quiz_completed' in session:
        return redirect('/results')

    # Ensure the user cannot manipulate the URL to access questions out of order
    if request.method == 'GET':
        current_index = int(request.args.get('index', 0))
        if current_index >= len(questions):
            return redirect('/results')

        # Check if the user has answered all preceding questions
        for i in range(current_index):
            if f'Question{i + 1}' not in session:
                return redirect(f'/questions?index={i}')  # Redirect to the first unanswered question

    if request.method == 'POST':
        current_index = int(request.form['current_index'])
        choice = request.form['choice']
        
        # Save response in session
        session[f'Question{current_index + 1}'] = choice

        if 'next_button' in request.form:
            # Check if a choice is selected
            if choice == "":
                return redirect(f'/questions?index={current_index}&error=1')  # Include error message
            next_index = current_index + 1
            if next_index >= len(questions):
                # Save all responses to the database
                user_data = {key: session[key] for key in session if key.startswith('Question')}
                user_data['Name'] = session.get('name')
                user_data['Age'] = session.get('age')
                db.results.insert_one(user_data)
                # Set session variable to indicate quiz completion
                session['quiz_completed'] = True
                return redirect('/results')
            else:
                return redirect(f"/questions?index={next_index}")

    current_index = int(request.args.get('index', 0))
    if current_index >= len(questions):
        return redirect('/results')
    
    current_question = questions[current_index]
    total_questions = len(questions)
    
    # Retrieve selected choice from session, if any
    selected_choice = session.get(f'Question{current_index + 1}', '')
    is_last_question = (current_index == total_questions - 1)

    return render_template('questions.html', current_question=current_question, current_index=current_index, total_questions=total_questions, selected_choice=selected_choice, is_last_question=is_last_question)


@quiz_bp.route("/clear_question_session", methods=['GET'])
def clear_question_session():
    # Clear only question-related data
    for key in list(session.keys()):
        if key.startswith('Question'):
            session.pop(key)
    # Remove the quiz completed flag from the session
    session.pop('quiz_completed', None)
    return redirect('/questions')