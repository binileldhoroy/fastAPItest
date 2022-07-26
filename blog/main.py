from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(engine)

@app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blog'])
def create(request: schemas.Blog,db:Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog',response_model = List[schemas.showBlog] ,tags=['blog'])
def getBlog(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',status_code=200,response_model=schemas.showBlog,tags=['blog'])
def getSingle(id,response:Response,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'error':'blog not found'}

    return blog


@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blog'])
def delete(id,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blog'])
def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    blog.title = request.title
    blog.body = request.body
    db.commit()
    return 'updated'


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

@app.post('/user',response_model=schemas.ShowUser,tags=['user'])
def createUser(request:schemas.User,db:Session=Depends(get_db)):
    hash_password = get_password_hash(request.password)
    new_user = models.User(name=request.name,email=request.email,password=hash_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}',response_model=schemas.ShowUser,tags=['user'])
def getUser(id,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user