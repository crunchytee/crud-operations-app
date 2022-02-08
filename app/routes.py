from crypt import methods
from urllib import response
from app import db
# from crud_operations_app import app
from app.models import User
from flask import request, Blueprint

bp = Blueprint("routes", __name__)

# GET all users
@bp.route("/all", methods=["GET"])
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
@bp.route("/signup", methods=["POST"])
def signup():

    # import pdb; pdb.set_trace()
    
    # Get response from signup
    body = request.json
    response_username = body["username"]
    response_password = body["password"]
    response_email_address = body["email-address"].lower()

    # Stage data for database
    u = User(email=response_email_address, username=response_username)
    u.set_password(response_password)
    db.session.add(u)

    # Commit new user to database
    db.session.commit()

    # For testing purposes
    # with open("log.txt", "a") as o:
    #     o.write(f"type of body is: {type(body)}\n")
    # return "complete", 200
    return {"username": response_username, "password": response_password, "email address": response_email_address}, 200

# Login
@bp.route("/login", methods=["POST"])
def login():

    # Get response from login form
    body = request.json
    response_email_address = body["email-address"]
    response_password_hash = body["password"]

    # Check submission against db
    u = User.query.filter_by(email=response_email_address).first()

    # If user or password wrong, return 401
    if u is None or not u.check_password(response_password_hash):
        return {"message": "Invalid username or password"}, 401
    
    # Here's where back end user session info would go
    # something like login_user(user)
    return {"message": "Logging in..."}, 200


# Update a User
@bp.route("/edit", methods=["PUT"])
def edit():
    # Get data from edit request
    body = request.json
    response_email = body["email"]
    response_username = body["username"]
    response_password = body["password"]

    user_to_edit = User.query.filter_by(email=response_email).first()
    if (response_username != user_to_edit.username):
        user_to_edit.username = response_username
    if (response_password != user_to_edit.password_hash):
        # To do: implement password hash
        user_to_edit.password_hash = response_password
    db.session.commit()
    # import pdb; pdb.set_trace()
    return {f"value": f"email: {response_email}, username: {response_username}, password: {response_password}"}, 200

# Delete a user
@bp.route("/delete", methods=["DELETE"])
def delete():
    # Get data from delete request
    body = request.json
    response_email = body["email"]

    # Query database
    user_to_delete = User.query.filter_by(email=response_email).first()

    # delete user if they exist
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
        return {"value": f"User {response_email} deleted successfully"}, 200
        # User.query.filter_by(email=response_email).delete(response_email, synchronize_session = False)
    else: 
        return {"value": f"User {response_email} not found"}, 200
    
