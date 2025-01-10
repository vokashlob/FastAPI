from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(CreateUser):
    pass


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int
    user_id: int


class UpdateTask(CreateTask):
    pass
