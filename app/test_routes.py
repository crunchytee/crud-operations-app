from __future__ import absolute_import

import pytest
from app.models import User
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
            yield client
            db.session.close()

def test_all(client):

    # Add two users to the db
    user1 = User(username="johndoe", password_hash="Password1!", email="johndoe@gmail.com")
    user2 = User(username="johndoe2", password_hash="Password1!", email="johndoe2@gmail.com")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Get users via /all route
    response = client.get(f"/all")
    json_response = response.get_json()
    users = json_response["users"]
    # import pdb; pdb.set_trace()

    # Assert retrieved data is the same as added data
    assert len(users) == 2
    assert users[0]["email"] == "johndoe@gmail.com"
    assert users[0]["username"] == "johndoe"
    assert users[0]["password"] == "Password1!"
    assert users[1]["email"] == "johndoe2@gmail.com"
    assert users[1]["username"] == "johndoe2"
    assert users[1]["password"] == "Password1!"

def test_signup(client):

    # Using the signup route, post a new user to the db
    client.post("/signup", json = {
        "username": "johndoe",
        "email-address": "johndoe@gmail.com",
        "password": "Password1!"
    })

    # Query the database and confirm that the user was signed up
    result = User.query.filter_by(username="johndoe").first()

    # Assertions
    assert result.username == "johndoe"
    assert result.check_password("Password1!") == True
    assert result.email == "johndoe@gmail.com"

def test_edit(client):

    # Create a user and commit to db
    user1 = User(username="johndoe", password_hash="Password1!", email="johndoe@gmail.com")
    db.session.add(user1)
    db.session.commit()

    # PUT change using /edit route
    client.put("/edit", json = {
        "username": "johndoe2",
        "email": "johndoe@gmail.com",
        "password": "Password1!2"
    })

    # Query change from db
    user1Changed = User.query.filter_by(email="johndoe@gmail.com").first()

    # Assertions
    assert user1Changed.username == "johndoe2"
    assert user1Changed.check_password("Password1!2") == True
    assert user1Changed.email == "johndoe@gmail.com"

def test_delete(client):

    # Create a user and commit to db
    user1 = User(username="johndoe", password_hash="Password1!", email="johndoe@gmail.com")
    db.session.add(user1)
    db.session.commit()

    # DELETE user using /delete route
    client.delete("/delete", json = {
        "email": "johndoe@gmail.com",
    })

    # Query db for deleted user
    response = User.query.filter_by(email="johndoe@gmail.com").first()
    # import pdb; pdb.set_trace()

    # Assertions
    assert type(response) == type(None)