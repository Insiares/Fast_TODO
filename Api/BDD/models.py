import os
import supabase
from supabase import create_client, Client
import datetime
from functools import wraps
from dotenv import load_dotenv
import yaml

with open('/home/insia/Simplon/13b_FastAPI/Fast_TODO/Api/BDD/.credentials.yml') as f:
    creds=yaml.load(f, Loader=yaml.FullLoader)

# load_dotenv(dotenv_path='./credentials.env')

url = creds["DB_URL"]
key = creds["PWD_DB"]

supa = create_client(url, key)


''' def(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs["supabase"] = supa
        return func(*args, **kwargs)
    return wrapper '''



def insert_db(tab, data, supabase=supa):
    """
    Insert data into desired table

    Parameters:
    tab (string): name of the table to insert in.
    data (dict): a dict with the values to insert.
        for users table :{"username": "<name>", "password": "<password>"}
        for tasks table :{"title": "<name>", "description": "<name>", 'due_date':"YYYY-MM-DD", "completed": "TRUE/FALSE", "user_id":<int>}

    Returns:
    supabase response.
    """
    response = (
    supabase.table(tab)
    .insert(data)
    .execute()
    )
    return response



def fetch_tasks(user_id, supabase=supa):
    """
    fetch tasks table

    Parameters:
    user_id (int): user id of the signed in user.
    
    Returns:
    (list of dict) All the tasks from the signed in user.
    """
    response = (supabase.table("tasks")
    .select("*")
    .eq("user_id", user_id)
    .execute()
    )
    return response


def fetch_users(username, supabase=supa):
    """
    fetch users table

    Parameters:
    user_id (int): user id of the signed in user.
    
    Returns:
    (dict) name and password of the signed in user.
    """
    response = (supabase.table("users").select("*")
    .eq("username", username)
    .execute()
    )
    return response


def complete_task(task_id, supabase=supa):
    """
    Turn the completed column of a task from FALSE to TRUE

    Parameters:
    task_id (int): the selected task id
    
    Returns:
    supabase response.
    """
    response = (
    supabase.table("tasks")
    .update({"completed": "TRUE"})
    .eq("id", task_id)
    .execute()
    )
    return response


def update_tab(tab, col, val, id, supabase=supa):
    """
    Replace a value in a selected table

    Parameters:
    tab (string): name of the table
    col (string): name of the column to replace
    val (string): new value
    id (int): id of the row where the value to replace is
    
    Returns:
    supabase response.
    """
    response = (
    supabase.table(tab)
    .update({col : val})
    .eq("id", id)
    .execute()
    )
    return response



def delete_row(tab, id, supabase=supa):
    """
    delete a complete row in a selected table

    Parameters:
    tab (string): name of the table
    id (int): id of the row to delete
    
    Returns:
    supabase response.
    """
    response = (
    supabase.table(tab)
    .delete()
    .eq("id", id)
    .execute()
    )
    return response

