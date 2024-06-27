import os
import supabase
from supabase import create_client, Client
import datetime
from functools import wraps
from dotenv import load_dotenv

load_dotenv(dotenv_path='credentials.env')

url = os.environ.get("DB_URL")
key = os.environ.get("PWD_DB")

supa = create_client(url, key)


def add_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs["supabase"] = supa
        return func(*args, **kwargs)
    return wrapper

@add_args
def insert_db(tab, data, supabase=None):
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


@add_args
def fetch_tasks(user_id, supabase=None):
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

@add_args
def fetch_users(user_id, supabase=None):
    """
    fetch users table

    Parameters:
    user_id (int): user id of the signed in user.
    
    Returns:
    (dict) name and password of the signed in user.
    """
    response = (supabase.table("users").select("*")
    .eq("user_id", user_id)
    .execute()
    )
    return response

@add_args
def complete_task(task_id, supabase=None):
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

@add_args
def update_tab(tab, col, val, id, supabase=None):
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


@add_args
def delete_row(tab, id, supabase=None):
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
