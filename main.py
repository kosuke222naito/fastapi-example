from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


class Input(BaseModel):
    name: str
    age: int


class User(BaseModel):
    id: int
    name: str
    age: int


app = FastAPI()


@app.get("/health")
async def health():
    return dict(status="ok")


@app.post("/users", response_model=User)
async def create_user(input: Input) -> User:
    return User.model_validate(
        dict(
            name=input.name,
            age=input.age,
            id=1,
        )
    )


@app.get("/users", response_model=List[User])
async def users() -> List[User]:
    return [
        User.model_validate(
            dict(
                name="John",
                age=30,
                id=1,
            )
        )
    ]


@app.get("/")
async def root():
    return {"greeting": "Hello World!"}
