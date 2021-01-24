from flask import Flask, redirect, url_for, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from insta import run
from werkzeug.exceptions import *
import datetime
import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')
app.secret_key = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
unfollowers = []
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String(), nullable=False, default=datetime.datetime.now)

    def __init__(self, username, quantity):
        self.username = username
        self.quantity = quantity

    def __repr__(self):
        return f"User('{self.username}', '{self.quantity}', '{self.date}', '{self.time}')"
db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            session.clear()
            unfollowers = []
            username = request.form["username"]
            session["username"] = username
            visibility = request.form["visibility"]
            session["visibility"] = visibility
            if username == '': 
                abort(422)
            return redirect(url_for("load"))
        finally:
            pass
    else:
        return render_template("index.html", ufill=True, vfill=True)

@app.errorhandler(422)
def no_username(e):
    # for only no username
    return render_template("index.html", ufill=False, vfill=True)

@app.errorhandler(400)
def no_visibility(e):
    # for no username and public/private
    if session["username"] == '':
         return render_template("index.html", ufill=False, vfill=False)
    # for no public/private
    return render_template("index.html", ufill=True, vfill=False)

@app.errorhandler(500)
def internalerror(e):
    return redirect(url_for("home"))


@app.route("/loading", methods=["GET", "POST"])
def load():
    return render_template("loading.html")

@app.route("/slow")
def slow():
    global unfollowers
    utrue = "username" in session
    vtrue = "visibility" in session
    if utrue and vtrue:
        usr = session["username"]
        vis = session["visibility"]
        unfollowers = run(usr,vis)
        return "very slow"
    else:
        return redirect(url_for("home"))


@app.route("/result", methods=["GET", "POST"])
def result():
    global unfollowers, db
    if unfollowers == ['PRIVATEREQUEST'] or unfollowers == ['PRIVATEIDIOT']:
        db.session.add(User(session["username"], -1))
    else:
        db.session.add(User(session["username"], len(unfollowers)))
    db.session.commit()
    return render_template("result.html", name=session["username"], list=unfollowers)

if __name__ == "__main__":
    app.run()
