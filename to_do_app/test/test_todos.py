from fastapi import status
from ..routers.todos import get_db,get_current_user
from .utils import *
from ..models import Todos

app.dependency_overrides[get_db]=override_get_db
app.dependency_overrides[get_current_user]=override_get_current_user



def test_read_all_authenticated(test_todo):
    response = client.get("/todos")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
        'complete': False,
        'title': 'learn to code',
        'description': 'because it is fun',
        'id': 1,
        'priority': 1,
        'owner_id': 1
    }]


def test_read_one_authenticated(test_todo):
    response = client.get("/todos/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'complete': False,
        'title': 'learn to code',
        'description': 'because it is fun',
        'id': 1,
        'priority': 1,
        'owner_id': 1
    }

def test_read_one_authenticated_not_found(test_todo):
    response = client.get("/todos/todo/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found.'}

def test_create_new_todo(test_todo):
    request_data = {'title': 'New todo is here ', 'description': 'because it is fun', 'priority': 5,'complete':False}
    response = client.post("/todos/todo", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

    db = Testing_Session_local()
    model = db.query(Todos).filter(Todos.id == 2).first()
    assert model.title == request_data['title']
    assert model.description == request_data['description']
    assert model.priority == request_data['priority']
    assert model.complete == request_data['complete']

def test_update_todo(test_todo):
    request_data = {'title': 'New updated todo is here ', 'description': 'because we have to change', 'priority': 3, 'complete': False}
    response = client.put("/todos/todo/1",json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = Testing_Session_local()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model.title == 'New updated todo is here '
    assert model.description == 'because we have to change'
    assert model.priority == 3
    assert model.complete == False


def test_update_todo_not_found(test_todo):
    request_data = {'title': 'New updated todo is here ', 'description': 'because we have to change', 'priority': 3, 'complete': False}
    response = client.put("/todos/todo/999",json=request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail':'Todo not found.'}

def test_delete_todo(test_todo):
    response = client.delete('/todos/todo/1')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = Testing_Session_local()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None

def test_delete_todo_not_found(test_todo):
    response = client.delete('/todos/todo/122')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail':'Todo not found.'}