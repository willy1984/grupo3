from flask import Flask, render_template, request
from databases.db import *

app = Flask(__name__)

@app.route("/")
def home_func():
    return render_template("activities.html")


@app.route("/consult_page")
def consult_page_func():
    return "Vista de consultar"

@app.route("/register_activity", methods=["post"])
def register_render_func():
    data = request.form
    name_activity = data["activityName"]
    start_time = data["startTime"]
    end_time = data["endTime"]
    duration = data["duration"]
    date_activity = data["date"]
    description_activity = data["description"]
    responsible = data["responsible"]
    project = data["platform"]
    add_activities(name_activity, start_time, end_time, duration, date_activity, description_activity, responsible, project)
    return "The activity was added"    

if __name__ == "__main__":
    host = '172.31.45.102'
    port = '80'
    app.run(host, port)