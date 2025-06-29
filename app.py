from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append({'task': todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    if 0 <= todo_id < len(todos):
        del todos[todo_id]
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>')
def toggle(todo_id):
    if 0 <= todo_id < len(todos):
        todos[todo_id]['done'] = not todos[todo_id]['done']
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>', methods=['POST'])
def edit(todo_id):
    new_task = request.form.get('task') 
    if 0 <= todo_id < len(todos):
        todos[todo_id]['task'] = new_task  
    return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run(debug=True)
