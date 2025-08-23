from flask import Flask, render_template, redirect, request, session
from flask_session import Session

app = Flask(__name__)
app.config["TEMPLATE_AUTO_RELOAD"] = True

# Uncomment the following if you want to use sessions
# 
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

@app.route("/")
def index():
    return render_template("pages/index.html")