from fastapi import FastAPI, Query
app = FastAPI()

class Game:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def modify_price(self, price):
        self.price = price

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.games = {}
        self.game_counter = 0

    def add_game(self, game):
        self.games[self.game_counter] = game
        self.game_counter += 1
        return self.game_counter - 1

    def remove_game(self, id):
        del self.games[id]

store = Store("SUPER_SKLEP")

@app.post("/add_game/")
async def hello_world(name: str, price: float):
    game = Game(name, price)
    game_id = store.add_game(game)
    return f"Game {name} added as id: {game_id}"

@app.get("/display_games/")
async def hello_world():
    return store.games

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)

    print("sigma skibidi")