from app import app, db
from app.models import User
from flask import request

# GET all users
@app.route("/all", methods=["GET"])
def all():
    # Query db for Users
    users = User.query.all()
    response = list()

    # Structure Users data
    for u in users:
        # response[str(u.username)] = {"email": str(u.email), "username": str(u.username), "password": str(u.password_hash)}
        response.append({"id": str(u.id), "email": str(u.email), "username": str(u.username), "password": str(u.password_hash)})

    return {"users": response}, 200

# POST a new user
@app.route("/signup", methods=["POST"])
def signup():

    # Get response from signup
    body = request.json
    response_username = body["username"]
    response_password = body["password"]
    response_email_address = body["email-address"]

    # Stage data for database
    u = User(email=response_email_address, username=response_username, password_hash=response_password)
    db.session.add(u)

    # Commit new user to database
    db.session.commit()

    # For testing purposes
    # with open("log.txt", "a") as o:
    #     o.write(f"type of body is: {type(body)}\n")
    # return "complete", 200
    return {"username": response_username, "password": response_password, "email address": response_email_address}, 200
