import os
from flask import Flask, render_template, request, flash,  url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

app.config['MONGO_URI'] = 'mongodb+srv://Duke:Kingdong20@recipewebappcluster.crmag.mongodb.net/mydb?retryWrites=true&w=majority'
mongo = PyMongo(app)

todos = mongo.db.todosapp

@app.route('/')
def index():
    saved_todos = todos.find()
    return render_template('index.html', todos=saved_todos)

@app.route('/add', methods=['POST'])
def add_todo():
    new_todo = request.form.get('new-todo')
    todos.insert_one({'text' : new_todo, 'complete' : False})
    return redirect(url_for('index'))

@app.route('/complete/<oid>')
def complete(oid):
    todo_item = todos.find_one({'_id': ObjectId(oid)})
    status = todo_item['complete']
    updated_value = { '$set' :
        {'complete': True}
    }
    todos.update_one(todo_item, updated_value)
    print(todo_item)
    return redirect(url_for('index'))

@app.route('/delete_completed')
def delete_completed():
    todos.delete_many({'complete' : True})
    return redirect(url_for('index'))

@app.route('/delete_all')
def delete_all():
    todos.delete_many({})
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)