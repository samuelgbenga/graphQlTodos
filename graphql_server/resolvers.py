from sqlite3 import dbapi2
from sqlalchemy import Column
from strawberry import ID
from . import schemas
from typing import List
from model import models
from config.database import DBSession


class QueryResolver:
    @staticmethod # same as static method in java they belong to the class
    def get_tasks(pagination:(schemas.PaginationInput|None) = None) -> List[schemas.Task]:
        # TODO: Connect to the database layer
        # TODO: update the pagination type
        db = DBSession()
        try:
            query = db.query(models.Task)

            if pagination is not None:
                query = query.offset(pagination.offset).limit(pagination.limit)
            
            tasks = query.all()
        
        finally:
            db.close()

        return tasks # type: ignore
        

    @staticmethod
    def get_task(task_id: ID) -> (schemas.Task | None):
        # TODO: Connect to the data layer
        db = DBSession()

        try:
            task = db.query(models.Task).filter(models.Task.id == task_id).first()

        finally:
            db.close()

        return task


class MutationResolver:
    @staticmethod
    def add_task(task_content: str) -> schemas.Task:
        # TODO: Connect to the data layer
        db = DBSession()
        try:
            new_task = models.Task(content = task_content)
            db.add(new_task)
            db.commit()
            db.refresh(new_task)
        finally:
            db.close()
        
        return new_task

    @staticmethod
    def update_task(task_id: ID, task: schemas.UpdateTaskInput) -> schemas.Task | None:
        # TODO: Connect to the data layer
        # TODO: update the task type

        db = DBSession()
        try:
            modified_task= db.query(models.Task).filter(models.Task.id == task_id).first()

            modified_task.content = task.content if task.content is not None else modified_task.content # type: ignore
            modified_task.is_done = task.is_done if task.is_done is not None else modified_task.is_done # type: ignore
            db.commit()
            db.refresh(modified_task)
        finally:
            db.close()

    @staticmethod
    def delete_task(task_id: ID) -> None:
        # TODO: Connect to the data layer
        db = DBSession()
        try:
            deleted_task = db.query(models.Task).filter(models.Task.id == task_id).first()
            db.delete(deleted_task)
            db.commit()
        finally:
            db.close()
        
