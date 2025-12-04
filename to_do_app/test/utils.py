from sqlalchemy import create_engine, StaticPool, text
from sqlalchemy.orm import sessionmaker
from ..database import Base
import pytest
from fastapi.testclient import TestClient
from ..main import app
from ..models import Todos,Users
from ..routers.auth import bcrypt_context

SQLALCHEMY_DATABASE_URl = 'sqlite:///./test.db'
engine = create_engine(SQLALCHEMY_DATABASE_URl, connect_args={"check_same_thread": False},poolclass=StaticPool)
Testing_Session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = Testing_Session_local()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {'username': 'test','id':1,'user_role':'admin'}





client = TestClient(app)

@pytest.fixture()
def test_todo():
    todo = Todos(title ="learn to code",description = "because it is fun",priority =1,complete = False,owner_id=1)
    db = Testing_Session_local()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE from todos;"))
        connection.commit()

@pytest.fixture()
def test_user():
    user = Users(
        username="Prashant1",
        email="prashant1@gmail.com",
        first_name="Prashant1",
        last_name="baral",
        hashed_password=bcrypt_context.hash("testpassword"),
        role="admin",
        phone_number="0123456789"
    )
    db = Testing_Session_local()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE from users;"))
        connection.commit()
