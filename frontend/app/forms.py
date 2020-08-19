from flask_wtf import FlaskForm
from wtform import StringField
from wtform.validators import DataRequired, SubmitField

class ScheduleForm(FlaskForm):
    time=StringField('schedule', validators=[DataRequired()])
    circuit=StringField('circuit name', validators=[DataRequired()])
    submit= SubmitField('Enter')
