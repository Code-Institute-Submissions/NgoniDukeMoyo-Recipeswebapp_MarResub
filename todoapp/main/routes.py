from flask import Blueprint, render_template, redirect, url_for, request

from todoapp.extentions import mango

main = Blueprint('__name__')

@main.route('/')
def index():
    todo_collection = mango.db.todosapp
    todosapp = todo_collection.find()
    return render_template('index.html', todo=todos)

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todo_collection = mango.db.todosapp
    todo_item = request.form.get('get-todo')
    todo_collection.insert_one({'text': todo_item, 'complete': False})
    return redirect(url_for('main.index'))

@main.route('/complete_todo/<oid>')
def complete_todo(oid):
    return redirect(url_for('main.index'))