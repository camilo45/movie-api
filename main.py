from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from config.database import  engine, Base
from middlewares.error_hadler import ErrorHandler
from routes.movie import movie_router
from utils.jwt_manger import create_token
from routes.user import user_router
import uvicorn


app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

#app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)



@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


if __name__ == '__main__':
   uvicorn.run("main:app", host="127.0.0.1", port=80, log_level="info", reload=True) 
