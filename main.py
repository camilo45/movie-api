from config.database import  engine, Base
#from middlewares.error_hadler import ErrorHandler
from routes.movie import movie_router
from routes.user import user_router
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")

app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

#app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


#app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)


@app.get ("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html",{
        "request":request,
        "message": "Hola gente, esta es my api con FastAPI"
        })

if __name__ == '__main__':
   uvicorn.run("main:app", host="0.0.0.0",port=10000, log_level="info", reload=True) 