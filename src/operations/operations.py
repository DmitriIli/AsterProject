from pydantic import BaseModel
from ..main import app


users_list = [
    {'id': 1, 'role': 'admin', 'name': 'admin'},
    {'id': 2, 'role': 'user', 'name': 'user'},
    {'id': 3, 'role': 'manager', 'name': 'manager'},
    {'id': 4, 'role': 'client', 'name': 'client'},
]

class User(BaseModel):
    id:int
    role:str
    name:str


@app.get('/')
def hello():
    return 'Hello'

@app.get('/users/{usr_id}')
def get_user(usr_id: int):
    try:
        return users_list[usr_id-1]
    except Exception as e:
        return e.__repr__


@app.get('/users/', response_model= List[User])
def get_users(limit: int, offset: int):
    return users_list[offset:][:limit]


@app.post('/users/{usr_id}', response_model=List[User])
def add_user(usr_id:int):
    print([user['id'] for user in users_list])
    if usr_id not in [user['id'] for user in users_list]:
        users_list.append(
            {'id': usr_id, 'role': 'some role', 'name': 'some name'})

    return users_list


@app.delete('/users/{usr_id}')
def delete_user(usr_id: int):
    try:
        users_list.remove(users_list[usr_id-1])
        return users_list

    except Exception as e:
        return 'do not exist'
