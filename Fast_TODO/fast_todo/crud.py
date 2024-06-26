# fast_todo/crud.py
#  Fonctions CRUD  qui interagissent avec la BDD
from sqlalchemy.orm import Session
from fast_todo import models, schemas, auth

def get_user(db: Session, user_id: int):
    try:
        return db.query(models.User).filter(models.User.id == user_id).first()
    except Exception as e:
        print(f"Erreur lors de la récupération de l'utilisateur par ID: {e}")
        return None

def get_user_by_username(db: Session, username: str):
    try:
        return db.query(models.User).filter(models.User.username == username).first()
    except Exception as e:
        print(f"Erreur lors de la récupération de l'utilisateur par nom d'utilisateur: {e}")
        return None

def create_user(db: Session, user: schemas.UserCreate):
    try:
        hashed_password = auth.get_password_hash(user.password)
        db_user = models.User(username=user.username, password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print(f"Erreur lors de la création de l'utilisateur: {e}")
        return None

def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    try:
        return db.query(models.Task).filter(models.Task.user_id == user_id).offset(skip).limit(limit).all()
    except Exception as e:
        print(f"Erreur lors de la récupération des tâches: {e}")
        return []

def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    try:
        db_task = models.Task(**task.dict(), user_id=user_id)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    except Exception as e:
        print(f"Erreur lors de la création de la tâche: {e}")
        return None

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    try:
        db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
        if db_task:
            for key, value in task.dict().items():
                setattr(db_task, key, value)
            db.commit()
            db.refresh(db_task)
        return db_task
    except Exception as e:
        print(f"Erreur lors de la mise à jour de la tâche: {e}")
        return None

def delete_task(db: Session, task_id: int):
    try:
        db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
        if db_task:
            db.delete(db_task)
            db.commit()
        return db_task
    except Exception as e:
        print(f"Erreur lors de la suppression de la tâche: {e}")
        return None

def get_task(db: Session, task_id: int):
    try:
        return db.query(models.Task).filter(models.Task.id == task_id).first()
    except Exception as e:
        print(f"Erreur lors de la récupération de la tâche par ID: {e}")
        return None
