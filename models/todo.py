import peewee as pw
from models.base_model import BaseModel
from models.user import User

class Todo(BaseModel):
   text = pw.CharField(unique=False)
   imageUrl = pw.CharField(unique=True)
   is_completed = pw.BooleanField(default=False)
   user_id = pw.ForeignKeyField(User, backref='images')
