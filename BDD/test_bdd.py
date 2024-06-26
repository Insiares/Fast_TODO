import os
import supabase
from supabase import create_client, Client
import datetime

url = DB_URL
key = PWD_DB
supabase = create_client(url, key)



response = (
    supabase.table("users")
    .insert({"id": 1, "username": "La poule", "password": "ViveLesCoqs"})
    .execute()
)

response = (
    supabase.table("users")
    .insert({"id": 2, "username": "Le caniche", "password": "Ouaf"})
    .execute()
)

response = (
    supabase.table("tasks")
    .insert({"id": 1, "title": "Pondre un oeuf", "description": "je pond mon oeuf dans la boite", 'due_date':"2024-06-06", "completed": "FALSE", "user_id":"1"})
    .execute()
)