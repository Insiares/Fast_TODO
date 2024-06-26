import os
import supabase
from supabase import create_client, Client
import datetime

url = "https://vbzkijbotwtkoyzufhik.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZiemtpamJvdHd0a295enVmaGlrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTk0MDI4MDMsImV4cCI6MjAzNDk3ODgwM30.38B1QxTfajCcBXyDbr-8FxyBjBmT1Gukt1CgfI2cWaY"
supabase = create_client(url, key)

response = supabase.auth.sign_in_with_password(
    credentials={"email": "fabien.soulavie@gmail.com", "password": "test"}
)

supabase.postgrest.auth(supabase.auth.get_session().access_token)

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