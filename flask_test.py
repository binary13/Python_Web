import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/about/")
def about_page():
    return render_template('about.html')


@app.route("/page2/")
def second_page():
    name = "Python"
    versions = [2.7, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5]
    return render_template('page2.html', name=name, versions=versions)


@app.route("/page3/")
def page3():
    return render_template('page3.html')


@app.errorhandler(404)
def four_oh_four(e):
    return render_template('404.html')

@app.errorhandler(500)
def four_oh_four(e):
    return render_template('404.html')


app.run(host="127.0.0.1", port=8080)
