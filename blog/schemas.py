
from pydantic import BaseModel

class Blog(BaseModel):  # pydantic
    title : str
    body : str