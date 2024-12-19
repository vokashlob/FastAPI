from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def read_root():
    return 'Главная страница'

@app.get('/user/admin')
async def admin():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def get_user(user_id: Annotated[int, Path(gt=0,
                                                ge=100,
                                                title="User ID",
                                                description="Enter user ID",
                                                example=1)]):
    return f'Вы вошли как пользователь №{user_id}'

@app.get('/user')
async def user_info(username, age):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
