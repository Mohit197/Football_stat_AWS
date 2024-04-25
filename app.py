from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello World'

@app.route("/questions", methods=['GET', 'POST'])
def question():
    if request.method == 'GET':
        return render_template('questions.html')
    elif request.method == 'POST':
        question1 = request.form['question1']
        print(question1)
        return redirect('/')
