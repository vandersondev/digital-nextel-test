from flask import Flask, render_template

app = Flask('app')

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/result/")
def result():
    return render_template('result.html')