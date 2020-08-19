from app import app
from flask import render_template
from app.forms import SchedulingForm


@app.route('/',methods=['GET',])
@app.route('/index')
def index():
    body = { 'teste' : "vamos la ver" }
    return render_template("index.html",title='Systema de rega',body=body)


@app.route('/forecast')
def forecast():
    return "you got into forecast"

@app.route('/schedule')
def scheduling (): 
    form=SchedulingForm()
    return render_template('schedule.html',title='Scheduling update', form=form)
