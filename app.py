from fastapi import FastAPI
import uvicorn
from logic import squares

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/squares/{n}")
async def get_squares(n: int):
    lst_of_squares = squares(n)
    return {"Squares": lst_of_squares}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")