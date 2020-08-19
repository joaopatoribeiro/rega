from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SchedulingForm(FlaskForm):
    time=StringField('schedule', validators=[DataRequired()])
    circuit=StringField('circuit name', validators=[DataRequired()])
    submit= SubmitField('Enter')
