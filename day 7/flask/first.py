from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

#routing
@app.route('/')
#view function: home
def home():
    return '<h1>Front Page! Hello</h1>'

@app.route('/backend/')
def next():
    return '<h1>I made a change</h1>'

#dynamic routing
# @app.route('/student/<string:name>/<int:text>')
# def student(name, text):
#     return '<h1>Hello, {}! This is the text {}. </h1>'.format(name, text)

@app.route('/student')
def stud():
    return render_template('student.html')

@app.route('/student/<name>')
def student(name):
    return render_template('student.html', name=name)

#Passing a dictionary to front end.
@app.route('/class')
def classInfo():
    class_info = {
        "members": ["Anna", "Sanjana"],
        "size": 2,
        "name": "Software Development"
    }
    return render_template('class.html', class_info=class_info)

# @app.route('/redirect')
# def redirect1():
#     return redirect(url_for('home'))

@app.route('/redirect')
def redirect1():
    return redirect("http://www.google.com")