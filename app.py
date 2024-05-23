from flask import Flask, render_template, request, redirect, session, make_response, jsonify
import bcrypt
from flask_pymongo import PyMongo
from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = "12ax12221zzx57z"


# Connect to MongoDB Atlas cluster
uri = "mongodb+srv://arslantariq931:Hashmap12@statsfootball.ujhfl7y.mongodb.net/?retryWrites=true&w=majority&appName=StatsFootball"
client = MongoClient(uri)
db = client.get_database('Football')



@app.route("/")
def home():
    if session.get('username'):
        name = session.get('name')  # Get the name from the session
        return render_template('home.html', name=name)
    else:
        return redirect('/login')


@app.route('/check_user_exists')
def check_user_exists():
    username = request.args.get('username')
    users = db.users
    existing_user = users.find_one({'name': username})
    return jsonify({'exists': existing_user is not None})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = db.users
        login_user = users.find_one({'username': request.form['username']})  # Change key to 'username'

        if login_user and bcrypt.checkpw(request.form['password'].encode('utf-8'), login_user['password']):
            session['username'] = request.form['username']
            session['name'] = login_user['name']  # Store the user's name in the session
            session['age'] = login_user['age']  # Store the user's age in the session
            return jsonify({'redirect': '/'})  # Redirect to home page
        else:
            return jsonify({'error': 'Invalid username/password combination'}), 400  # Return error with status code 400
    else:
        # Handle GET request
        return render_template('login.html')  # Render the login page for GET requests


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = db.users
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            # Hash the password
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            # Insert user details into the database
            users.insert_one({
                "username": request.form['username'],
                "name": request.form['name'],
                "age": int(request.form['age']),
                'password': hashpass
            })
            return redirect("/login")  # Redirect to login after successful registration
        return "That username already exists!"
    return render_template('register.html')


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response



@app.route("/about")
def about():
    return render_template('about.html')













def read_questions_from_file(file_path):
    questions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_question = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Q"):
                if current_question:
                    questions.append(current_question)
                current_question = {"text": "", "choices": []}
                question_parts = line.split(': ', 1)
                if len(question_parts) == 2:
                    current_question["text"] = question_parts[1].strip()
                else:
                    current_question["text"] = line
            else:
                current_question["choices"].append(line)
        if current_question:
            questions.append(current_question)
    return questions

questions = read_questions_from_file('questions.txt')

@app.route("/user")
def user():
    # Check if the user is logged in
    if 'name' not in session:
        return redirect('/login')
    
    # Check if the quiz is completed
    if 'quiz_completed' in session:
        return render_template('user.html')
    else:
        return redirect('/questions')


@app.route("/questions", methods=['GET', 'POST'])
def question():
    # Check if the user is logged in
    if 'name' not in session:
        return redirect('/login')
    
    # Check if the quiz is completed
    if 'quiz_completed' in session:
        return redirect('/user')

    # Ensure the user cannot manipulate the URL to access questions out of order
    if request.method == 'GET':
        current_index = int(request.args.get('index', 0))
        if current_index >= len(questions):
            return redirect('/user')

        # Check if the user has answered all preceding questions
        for i in range(current_index):
            if f'Question{i + 1}' not in session:
                return redirect(f'/questions?index={i}')  # Redirect to the first unanswered question

    if request.method == 'POST':
        current_index = int(request.form['current_index'])
        choice = request.form['choice']
        
        # Save response in session
        session[f'Question{current_index + 1}'] = choice
        
        next_index = current_index + 1
        if next_index >= len(questions):
            # Save all responses to the database
            user_data = {key: session[key] for key in session if key.startswith('Question')}
            user_data['Name'] = session.get('name')
            user_data['Age'] = session.get('age')
            db.results.insert_one(user_data)
            # Set session variable to indicate quiz completion
            session['quiz_completed'] = True
            return redirect('/user')
        else:
            return redirect(f"/questions?index={next_index}")

    current_index = int(request.args.get('index', 0))
    if current_index >= len(questions):
        return redirect('/user')
    
    current_question = questions[current_index]
    total_questions = len(questions)
    
    # Retrieve selected choice from session, if any
    selected_choice = session.get(f'Question{current_index + 1}', '')

    return render_template('questions.html', current_question=current_question, current_index=current_index, total_questions=total_questions, selected_choice=selected_choice)





@app.route("/clear_question_session", methods=['GET'])
def clear_question_session():
    # Clear only question-related data
    for key in list(session.keys()):
        if key.startswith('Question'):
            session.pop(key)
    # Remove the quiz completed flag from the session
    session.pop('quiz_completed', None)
    return redirect('/questions')
