from __future__ import absolute_import
import pytest
from app.models import User
from app import create_app, db


@pytest.fixture
def context():
    app = create_app()
    with app.app_context() as context:
        db.session.remove()
        db.drop_all()
        db.create_all()
        yield context
        db.session.close()

def test_add_user(context):
    # Create user and add to DB
    user = User(username="johndoe", password_hash="Password1!", email="johndoe@gmail.com")
    db.session.add(user)
    db.session.commit()
    result = User.query.filter_by(username="johndoe").first()
    # import pdb; pdb.set_trace()

    # Assertions
    assert result.username == "johndoe"
    assert result.password_hash == "Password1!"
    assert result.email == "johndoe@gmail.com"

def test_remove_user(context):
    # Create user and add to DB
    user = User(username="johndoe", password_hash="Password1!", email="johndoe@gmail.com")
    db.session.add(user)
    db.session.commit()
    result = User.query.filter_by(username="johndoe").first()

    # Assert user was really added
    assert result.username == "johndoe"
    assert result.password_hash == "Password1!"
    assert result.email == "johndoe@gmail.com"

    # Remove user and re-query
    db.session.delete(result)
    db.session.commit()
    result2 = User.query.filter_by(username="johndoe").first()

    # Assertions
    assert type(result2) == type(None)

def test_update_user(context):
    # Create user and add to DB
    user = User(username="johndoe", password_hash="Password1!", email="johndoe@gmail.com")
    db.session.add(user)
    db.session.commit()
    result = User.query.filter_by(username="johndoe").first()

    # Assert user was really added
    assert result.username == "johndoe"
    assert result.password_hash == "Password1!"
    assert result.email == "johndoe@gmail.com"

    # Update user
    result.username = "notjohndoe"
    result.password_hash = "notPassword1!"
    result.email = "notjohndoe@gmail.com"
    db.session.commit()

    # Re-query and assert
    result = User.query.filter_by(username="notjohndoe").first()
    assert result.username == "notjohndoe"
    assert result.password_hash == "notPassword1!"
    assert result.email == "notjohndoe@gmail.com"


