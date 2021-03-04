from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

#To-Do List App
todo_items = [0]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=["GET", "POST"])
def todo_add():
    if request.method == 'POST':
        new_todo = {
            'id': todo_items[0],
            'title': request.form['title'],
            'date': request.form['date'],
            'description': request.form['description']
        }
        #add to list / save in database
        todo_items.append(new_todo)
        #update the identifier
        todo_items[0] = todo_items[0] + 1
    return render_template('todo_add.html')

@app.route('/todo-list', methods=["GET"])
def todo_list():
    return render_template('todo_list.html', todo_items=todo_items)

# Delete
@app.route('/todo-list/delete', methods=["DELETE"])
def todo_item():
    req_response = request.get_json()
    req_id = int(req_response['id'])
    for item in todo_items[1:]:
        if item['id'] == req_id:
            todo_items.remove(item)
    print(todo_items)
    return str(req_id)

@app.route('/example')
def example_1():
    return render_template('get.html')
