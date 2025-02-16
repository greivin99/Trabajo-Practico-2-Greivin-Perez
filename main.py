from fastapi import FastAPI
from starlette import status
from pydantic import BaseModel

app = FastAPI(
    title = "First api post",
    description="First api post",
    version="0.0.1",
)

users = []

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/user")
def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully", "user": user}