from app import app
from app.models import User
from flask import request

@app.route("/all", methods=["GET"])
def all():
    users = User.query.all()
    response = dict()
    for u in users:
        response[str(u.username)] = {"username": str(u.username), "email": str(u.email)}
      
    return {"users": response}, 200

@app.route("/signup", methods=["POST"])
def signup():
    body = request.get_json()
    # response_username = body["username"]
    # response_password = body["password"]
    # with open("log.txt", "a") as o:
    #     o.write(f"username = {response_username}, password = {response_password} \n")
    # return f"username = {response_username}, password = {response_password}"
    return "success"
