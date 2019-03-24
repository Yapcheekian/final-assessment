import peewee as pw
from models.base_model import BaseModel

class Todo(BaseModel):
   text = pw.CharField(unique=False)
   imageUrl = pw.CharField(unique=True)
