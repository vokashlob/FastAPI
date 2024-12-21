from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int = None
    username: str
    age: int


users: List[User] = []


@app.get('/')
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {'request': request, 'users': users})


@app.get('/user/{user_id}')
async def get_users(request: Request, user_id: Annotated[int, Path(ge=1,
                                                                   title='User ID',
                                                                   description='Enter user ID',
                                                                   example='1')]) -> HTMLResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {'request': request, 'user': user})
    raise HTTPException(status_code=404, detail='User not found')


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5,
                                                  max_length=15,
                                                  title='User Name',
                                                  description='Enter user name',
                                                  example='UrbanUser')],
                    age: Annotated[int, Path(ge=18,
                                             le=110,
                                             title='User Age',
                                             description='Enter User Age',
                                             example='25')]) -> User:
    new_id = max((u.id for u in users), default=0) + 1
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1,
                                                   title='User ID',
                                                   description='Enter user ID',
                                                   example='1')],
                      username: Annotated[str, Path(min_length=5,
                                                    max_length=15,
                                                    title='User Name',
                                                    description='Enter user name',
                                                    example='UrbanUser')],
                      age: Annotated[int, Path(ge=18,
                                               le=110,
                                               title='User Age',
                                               description='Enter User Age',
                                               example='25')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1,
                                                   title='User ID',
                                                   description='Enter user ID',
                                                   example='1')]) -> User:
    for num, user in enumerate(users):
        if user.id == user_id:
            del users[num]
            return user
    raise HTTPException(status_code=404, detail='User not found')
