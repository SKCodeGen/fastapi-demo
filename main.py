from typing import Optional
from collections import OrderedDict
from fastapi import FastAPI
from request_data.user import User

import numpy as np

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


if __name__ == "__main__":
    list = [{"name": "anshul", "school": "basis"}, {"name": "aarnav", "school": "steiner"}, {"name": "aarush", "school": "steiner"}]

    names_dict = {student["name"]:student["school"] for student in list}
    order_dict = OrderedDict({student["name"]:student["school"] for student in list})
    print(names_dict)
    print(order_dict)
    print(order_dict.values())

    check_duplicate_key_dict = {"key0": "qe", "key1": "fv", "key3": "rh", "key1": "uu"}
    print(check_duplicate_key_dict)

    not_a_num = float("nan")
    print(not_a_num)
    print(f'not_a_num: {np.isnan(not_a_num)}')

    tup1 = (1, 2, 3)
    tup2 = (4, 5)
    print(tup1 + tup2)

