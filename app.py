from flask import Flask, render_template , abort 

app = Flask(__name__)

# i'll make a dummy task object so then i can mess around with the task obj on the front end
tasks = [ 
            ["Gigi Murin", "Justice", "Huh? But it was funny! Don't get mad at me!"],
            ["Shiori Novella", "Advent", "Don't you think that's a wonderful story?"],
            ["Ouro Kronii", "Promise", "Kroniichiwa! It's me, perfection. Also synonymous for Ouro Kronii!"],
            ["Mori Calliope", "Myth", "Dead Beats, listen up! Your Mori's been working hard for you!"],
            ["Raora Panthera", "Justice", "Woah, this place looks delicious! Let's go check it out!"],
            ["Koseki Bijou", "Advent", "I hope you'll feel my radiance!"]
        ]

@app.route('/home')
def home_page():    
    return render_template('home_page.html', tasks=tasks)

@app.route('/create_task', methods=["GET", "POST'"])
def create_task_page():
    return render_template('create_task.html')

@app.route('/tasks/<int:taskID>')
def task_view_page(taskID):
    try:
        return render_template('task_view.html', task=tasks[taskID])
    except:
        abort(404)

@app.errorhandler(404)
def you_messed_up(error):
    return render_template('404.html', err=error), 404