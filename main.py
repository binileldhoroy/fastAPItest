from re import A
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {'data':'hi'}

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