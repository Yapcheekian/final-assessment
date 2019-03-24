import datetime
from database import db
from flask_login import UserMixin
import peewee as pw


class BaseModel(pw.Model, UserMixin):
   created_at = pw.DateTimeField(default=datetime.datetime.now)
   updated_at = pw.DateTimeField(default=datetime.datetime.now)

   def save(self, *args, **kwargs):
       self.updated_at = datetime.datetime.now()
       return super(BaseModel, self).save(*args, **kwargs)

   class Meta:
       database = db
       legacy_table_names = False