from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from functions.sort import create_teams_list, assign_teams
from functions.make_dict import make_dict, list_to_string

app = Flask(__name__)
app.config["TEMPLATE_AUTO_RELOAD"] = True

# Uncomment the following if you want to use sessions
# 
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

sample_dict_return = {
    'status': 'success/fail/...',
    'leader_name_1': [],
    'leader_name_2': [],
    'leader_name_x': []
}

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route("/sort", methods=["GET", "POST"])
def sort():
    if request.method == "POST":
        leader_names = request.form.get('leaders').strip().replace('\r\n', ';').split(';')
        pots_list = list()
        pots_count = len(request.form) - 1

        for i in range(pots_count):
            pots_list.append(request.form.get(f'{i}_members').strip().replace('\r\n', ';').split(';'))

        teams = create_teams_list(leader_names)
        teams = assign_teams(teams,make_dict('pot',pots_list))

        for i in range(len(teams)):
            teams[i].members = list_to_string(teams[i].members)
            print(f'Team{i + 1}:\r\n{teams[i].members}')

        return render_template('pages/results.html', results=teams), 200

        # print(pots_list)

        return "", 200