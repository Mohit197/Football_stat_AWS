from flask import Flask, render_template, request, redirect, session
import bcrypt
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "12ax12221zzx57z"

# Database
app.config['MONGO_DBNAME'] = "Football"
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Football'

mongo = PyMongo(app)

@app.route("/")
def home():
    if 'username' in session:
        return render_template('home.html')
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})

        if login_user:
            if bcrypt.checkpw(request.form['password'].encode('utf-8'), login_user['password']):
                session['username'] = request.form['username']
                return redirect('/')
        return "Invalid username/password combination"
    return render_template('login.html')  # Render the login page for GET requests

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({"name": request.form['username'], 'password': hashpass})
            return redirect("/login")  # Redirect to login after successful registration
        return "That username already exists!"
    return render_template('register.html')












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


    
@app.route("/questions", methods=['GET', 'POST'])
def question():
    if request.method == 'GET':
        current_index = int(request.args.get('index', 0))
        current_question = questions[current_index]
        return render_template('questions.html', current_question=current_question, current_index=current_index)
    elif request.method == 'POST':
        current_index = int(request.form['current_index'])
        choice = request.form['choice']
        print(f"Question {current_index + 1}: {choice}")
        next_index = current_index + 1
        if next_index < len(questions):
            return redirect(f"/questions?index={next_index}")
        else:
            return redirect('/')
