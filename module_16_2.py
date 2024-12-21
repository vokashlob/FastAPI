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
async def get_user(user_id: int = Path(ge=1,
                                       le=100,
                                       title="user ID",
                                       description="Enter user ID",
                                       example='1')):
    return f'Вы вошли как пользователь №{user_id}'

@app.get('/user/{username}/{age}')
async def user_info(username: Annotated[str, Path(min_length=5,
                                                  max_length=20,
                                                  title='Username',
                                                  description='Enter username',
                                                  example='UrbanUser')],
                    age: Annotated[int, Path(ge=18,
                                             le=120,
                                             title='Age',
                                             description='Enter age',
                                             example='24')]):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
