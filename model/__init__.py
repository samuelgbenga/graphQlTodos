from pyexpat import model
from . import models
from config import database

# this will create the task table if it does not exist already

models.Base.metadata.create_all(bind=database.engine)

