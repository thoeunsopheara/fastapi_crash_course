
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = True



app = FastAPI()


@app.get('/')
def home():
    return {'data': 'Blogs list'}

@app.get('/about')
def about():
    return { 'data': { 'page': 'about page' } }

@app.get('/blog')
def shows(limit: int):
    return {'blogs': f'{limit} blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return { 'data': id }

@app.post('/blog')
def add_blog(blog: Blog):

    return {
        'data': {
            'title': f'blog title is {blog.title}',
            'body': blog.body,
            'published': blog.published
        }
    }
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=3500)
