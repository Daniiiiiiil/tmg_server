from fastapi import FastAPI
import random

app = FastAPI()

coordinates = dict()


@app.get("/hide")
def hide_treasure():
    coordinates["x"] = random.randrange(1, 100)
    coordinates["y"] = random.randrange(1, 100)
    return {"hided": True}


@app.get("/check/{username}+{x}+{y}")
def check_hit(username: str, x: int, y: int):
    responce = dict()
    responce["username"] = username
    responce["diffx"] = coordinates["x"] - x
    responce["diffy"] = coordinates["y"] - y

    diffs = ["diffx", "diffy"]
    for diff in diffs:
        if responce[diff] < 0:
            responce[diff] *= -1

    return responce
