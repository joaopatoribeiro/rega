from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    body = { 'teste' : "vamos la ver" }
    return render_template("index.html",title='pagina',body=body)


@app.route('/forecast')
def forecast():
    return "you got into forecast"
