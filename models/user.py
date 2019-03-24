import peewee as pw
from models.base_model import BaseModel


class User(BaseModel):
   name = pw.CharField(unique=True)
   email = pw.CharField(unique=True)
   password = pw.CharField(unique=True)