from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

class User(BaseModel):
    id: int = Field(default=None, description='User ID')
    username: str = Field(min_length=5, max_length=15, description='User name')
    age: int = Field(le=120, ge=18, description='Age')

users: List[User] = []

@app.get('/users', response_model=List[User])
async def get_users():
    return users

@app.post('/user/{username}/{age}', response_model=User)
async def post_user(username: str, age: int):
    new_id = max((u.id for u in users), default=0) + 1
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: int, username: str, age: int):
        for user in users:
                if user.id == user_id:
                    user.username = username
                    user.age = age
                    return user
        raise HTTPException(status_code=404, detail='User not found')

@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: int):
        for num, user in enumerate(users):
            if user.id == user_id:
                del users[num]
                return user
        raise HTTPException(status_code=404, detail='User not found')
