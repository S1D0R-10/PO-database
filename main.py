from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get('/test1{id}')
async def test1(id: int):
    return f'otrzymalem parametr{id}'

@app.post('/test2{id}')
async def test2(id: int):
    return f"dodalem do bazy{id}"

uvicorn.run(app, host='0.0.0.0', port=8000)