from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/home')
def landing_page():
    # i'll make a dummy task object so then i can mess around with the task obj on the front end
    tasks = [ ["Gigi Murin", "Justice", "Huh? But it was funny! Don't get mad at me!"],
                ["Shiori Novella", "Advent", "Don't you think that's a wonderful story?"]
            ]
        
    return render_template('home_page.html', tasks=tasks)

@app.route('/create_task')
def create_task_page():
    return render_template('create_task.html')

@app.route('/tasks/<int:taskID>')
def task_view_page(taskID):
    return render_template('task_view.html')