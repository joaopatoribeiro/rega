from app import app


@app.route('/')
@app.route('/index')
def index():
    return "hello website"


@app.route('/forecast')
def forecast():
    return "you got into forecast"
