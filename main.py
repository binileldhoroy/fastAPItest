from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit=10,published:bool=True, sort:Optional[str] = None):
    if published:
        return {'data':f'{limit} published blog from db'}
    else:
        return {'data':f'{limit} published blog'}

@app.get('/blog/unpublished')
def unpublished():
    #unpublished data
    return {'data':'unpublished'}

@app.get('/blog/{id}')
def show(id:int):
    #get some data with id
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    #to get comments of blog with id
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title : str
    description : str
    published : Optional[bool]

@app.post('/blog')
def createBlog(blog:Blog):
    return {'data': f'blog is created {blog.title}'}



#to change the port
#run the app with python main.py
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=9000)