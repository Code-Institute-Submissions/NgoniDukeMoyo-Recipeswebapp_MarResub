from flask_pymango import blueprint, render_template, redirect, url_for, request

from todosapp.extentions import mango

main = Blueprint('main', __name__)



@main.route('/')
def index():
    todos_collection = mango.db.todosapp
    todos = todos_collection.find()
    return render_template('index.html', todos = todos)

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todos_collection = mango.db.todosapp
    todo_item = request.form.get('add-todo')
    todos_collection.insert_one({'text': todo_item, 'complete' : False})
    return redirect(url_for('main.index'))


