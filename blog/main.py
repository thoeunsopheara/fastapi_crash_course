
from fastapi import FastAPI, Request


from . import models
from .database import engine
from .routers import blog, user, authentication


models.Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
async def serve_spa(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(blog.routers)
app.include_router(user.routers)
app.include_router(authentication.routers)
