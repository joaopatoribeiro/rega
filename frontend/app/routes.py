from app import app
from flask import render_template, url_for, flash, redirect 
from app.forms import SchedulingForm

@app.route('/',methods=['GET',])
@app.route('/index')
def index():
    body = { 'teste' : "vamos la ver" }
    return render_template("index.html",title='Systema de rega',body=body)


@app.route('/forecast')
def forecast():
    return "you got into forecast"

@app.route('/schedule',methods=['GET','POST'])
def scheduling (): 
    form=SchedulingForm()
    if form.validate_on_submit():
        flash(f'tu entraste of seguintes valores {form.time.data} e o circuito {form.circuit.data}')
        return redirect(url_for('index'))
    return render_template('schedule.html',title='Scheduling update', form=form)
