from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/home')
def landing_page():
    return "Hi hi hi hi hi"

@app.route('/create_task')
def create_task_page():
    return "to make a task, no not, that is my question to YOU"

@app.route('/tasks/<taskID>')
def task_view_page(taskID):
    return "Well, there is no task here. (yet)"