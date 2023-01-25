from fastapi import FastAPI
from game import Game

app = FastAPI()


@app.get("/hide")
def hide_treasure():
    new_game = Game()
    return {"game_id": new_game.get_id()}


@app.get("/check/{game_id}+{x}+{y}")
def check_hit(game_id: int, x: int, y: int):
    if Game.is_available(game_id):
        return {"match_rate": Game.check_hit(game_id, (x, y))}
    
    return {"err": "Game not found!"}
