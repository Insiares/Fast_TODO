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
    response = (
    supabase.table(tab)
    .insert(data)
    .execute()
    )
    return response


@add_args
def fetch_tasks(user_id, supabase=None):
    response = (supabase.table("tasks")
    .select("*")
    .eq("user_id", user_id)
    .execute()
    )
    return response

@add_args
def fetch_users(user_id, supabase=None):
    response = (supabase.table("users").select("*")
    .eq("user_id", user_id)
    .execute()
    )
    return response

@add_args
def complete_task(task_id, supabase=None):
    response = (
    supabase.table("tasks")
    .update({"completed": "TRUE"})
    .eq("id", task_id)
    .execute()
    )
    return response

@add_args
def update_tab(tab, col, val, id, supabase=None):
    response = (
    supabase.table(tab)
    .update({col : val})
    .eq("id", id)
    .execute()
    )
    return response


@add_args
def delete_row(tab, id, supabase=None):
    response = (
    supabase.table(tab)
    .delete()
    .eq("id", id)
    .execute()
    )
    return response

