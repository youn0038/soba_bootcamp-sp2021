from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

#To-Do List App
todo_items = [0]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=["GET", "POST"])
def todo_add():
    return render_template('todo_add.html')
    # if request.method == 'POST':

@app.route('/todo-list')