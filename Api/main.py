# main.py
# Point d'entrée de l'application FastAPI, définit les routes (endpoints).

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from Api import auth, schemas
from .BDD import models





app = FastAPI()
supa = models.ini_db()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    try:
        supa = models.ini_db()
        test_us = str(user.username)
        db_user = models.fetch_users(username=test_us,  supabase = supa)

        if db_user:
            raise HTTPException(status_code=400, detail="Nom d'utilisateur déjà enregistré")
        user.password = auth.get_password_hash(user.password)

        return models.insert_db('users', user.dict())

    except Exception as e:
        print(f"Erreur lors de la création de l'utilisateur: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f'Erreur interne du serveur : {e}'
        )

'''
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = crud.get_user_by_username(db, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Nom d'utilisateur ou mot de passe incorrect")
    return {"message": "Connexion réussie", "user_id": user.id}


@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db), user_id: int = 1):
    try:
        tasks = crud.get_tasks(db, user_id=user_id, skip=skip, limit=limit)
        return tasks
    except Exception as e:
        print(f"Erreur lors de la récupération des tâches: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur interne du serveur"
        )

@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db), user_id: int = 1):
    try:
        return crud.create_task(db=db, task=task, user_id=user_id)
    except Exception as e:
        print(f"Erreur lors de la création de la tâche: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur interne du serveur"
        )

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(database.get_db), user_id: int = 1):
    try:
        db_task = crud.get_task(db, task_id=task_id)
        if not db_task or db_task.user_id != user_id:
            raise HTTPException(status_code=404, detail="Tâche non trouvée")
        return crud.update_task(db=db, task_id=task_id, task=task)
    except Exception as e:
        print(f"Erreur lors de la mise à jour de la tâche: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur interne du serveur"
        )

@app.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(database.get_db), user_id: int = 1):
    try:
        db_task = crud.get_task(db, task_id=task_id)
        if not db_task or db_task.user_id != user_id:
            raise HTTPException(status_code=404, detail="Tâche non trouvée")
        return crud.delete_task(db=db, task_id=task_id)
    except Exception as e:
        print(f"Erreur lors de la suppression de la tâche: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur interne du serveur"
        )
'''
# Démarrage de l'application:
# uvicorn Api.main:app --reload

# documentation de l'API
# http://127.0.0.1:8000/docs
