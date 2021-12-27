from app import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello World!"

@app.route("/amazing")
def amazing():
    return "EPIC PAGE HERE"