import pytest
import sys
sys.path.append("..")

from app.models import User
from app import db

def test_add_user():
    # Create user and add to DB
    user = User(username="johndoe", password_hash="Password1!", email="johndoe@gmail.com")
    db.session.add(user)
    db.session.commit()

    result = User.query.filter_by(username="johndoe")
    assert result.username == "johndoe"
    assert result.password_hash == "Password1!"
    assert result.email == "johndoe@gmail.com"
