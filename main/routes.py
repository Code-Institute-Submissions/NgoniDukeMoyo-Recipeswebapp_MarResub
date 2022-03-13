from flask import Blueprint, render_template, redirect, url_for, request
from bson.objectid import ObjectId

from todoapp.extentions import mango

main = Blueprint('main', __name__)


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
    todos_collection = mango.db.todos
    todo_item = todos_collection.find_one({'_id': ObjectId(oid)})
    todo_item['complete'] = True
    todos_collection.save(todo_item)
    return redirect(url_for('main.index'))
  

@main.route('/delet_completed')
def delet_completed():
    todos_collection = mango.db.todos 
    todos_collection.delete_many({'complete': True})
    return redirect(url_for('main.index'))


@main.route('/delete_all')
def delete_all():
    todos_collection = mango.db.todos 
    todos_collection.delete_many({})
    return redirect(url_for('main.index'))
