import os
from supabase import create_client, Client
import datetime
import yaml
import logging
import json

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def ini_db():
    with open("/home/insia/Simplon/13b_FastAPI/Fast_TODO/Api/BDD/.credentials.yml") as f:
        creds = yaml.load(f, Loader=yaml.FullLoader)

    # load_dotenv(dotenv_path='./credentials.env')

    url = creds["DB_URL"]
    key = creds["PWD_DB"]
    logger.debug(f"Supabase URL: {url}")
    logger.debug(f"Supabase Key: {key}")
    supa = create_client(url, key)
    return supa

supabase = ini_db()

payload = { "username": "mon_vier"}
payload = json.dumps(payload)
try:
    response = supabase.table("users").select("*").eq("user_id", payload).execute()
    logger.debug("Response from Supabase: %s", response)
    print(response)
except Exception as e:
    logger.error(f"An error occurred: {e}")
    logger.error("Exception details:", exc_info=True)


def complete_task(task_id):
    response = (
    supabase.table("tasks")
    .update({"completed": "TRUE"})
    .eq("id", task_id)
    .execute()
    )
    return response













# def new_user_db(user, supabase=supabase):
#     response = (
#     supabase.table("users")
#     .insert(user)
#     .execute()
#     )
#     return response

# def insert_db(table, data):
#     response = (
#     supabase.table(table)
#     .insert(data)
#     .execute()
#     )
#     return response



# def fetch_task(table):
#     response = supabase.table(table).select("*").execute()
#     return response


#new_users_db({"username": "Le caniche", "password": "Onnesentpaslecul"})
# response=(supabase.table("users")
#           .select("username, id")
#           .eq("username","Le caniche")
#           .execute()
#           )
# print(response)

#new_task_db({"title": "Ronger un os", "description": "J'en laisse pas une miette", 'due_date':"2024-06-06", "completed": "FALSE", "user_id":"1"})

""" response = (
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
    .insert({"title": "Pondre un oeuf", "description": "je pond mon oeuf dans la boite", 'due_date':"2024-06-06", "completed": "FALSE", "user_id":"1"})
    .execute()
)


response = (
    supabase.table("tasks")
    .insert({"title": "Manger des graines", "description": "J'ai faim", 'due_date':"2024-06-07", "completed": "FALSE", "user_id":"1"})
    .execute()
)

response = (
    supabase.table("tasks")
    .insert({"title": "Manger un os", "description": "J'ai faim", 'due_date':"2024-06-07", "completed": "FALSE", "user_id":"2"})
    .execute()
) """

# response = (supabase.table("tasks").select("*")
#           .eq("user_id", 1)
#           .execute()
#           )


# print(response)