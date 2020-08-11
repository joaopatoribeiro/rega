import flask
import flask_lambda

app=flask_lambda.FlaskLambda(__name__)

from app import routes


