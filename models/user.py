import os
import peewee as pw
import datetime
from database import db

class BaseModel(pw.Model):
   created_at = pw.DateTimeField(default=datetime.datetime.now)
   updated_at = pw.DateTimeField(default=datetime.datetime.now)

   def save(self, *args, **kwargs):
       self.updated_at = datetime.datetime.now()
       return super(BaseModel, self).save(*args, **kwargs)

   class Meta:
       database = db
       legacy_table_names = False

class User(BaseModel):
   name = pw.CharField(unique=True)
   email = pw.CharField(unique=True)
   password = pw.CharField(unique=True)