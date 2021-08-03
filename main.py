from typing import Optional

from fastapi import FastAPI
from request_data.user import User

app = FastAPI()


@app.get("/")
def get_root():
    return {"demo": "Fast API"}


@app.get("/user/{user_id}")
def get_user(user_id: int, department: Optional[str] = None):
    return {"id": user_id, "name": "firstname lastname", "department": department}


@app.put("/user/{user_id}")
def update_user(user_id: int, user: User):
    return {"status": "success", "user_id": user_id, "user name": user.name}


