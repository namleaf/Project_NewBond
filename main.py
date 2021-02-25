import datetime
from datetime import date

import pandas as pd
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/child_growth")
def growth():
    return render_template('Growth.html')

@app.route("/admin")
def admin():
    return  redirect(url_for("home"))


if __name__ == "__main__":
    app.run()


