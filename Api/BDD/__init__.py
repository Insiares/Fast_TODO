import yaml
from supabase import create_client
from functools import wraps


with open('/home/insia/Simplon/13b_FastAPI/Fast_TODO/Api/BDD/.credentials.yml') as f:
    creds=yaml.load(f, Loader=yaml.FullLoader)

# load_dotenv(dotenv_path='./credentials.env')

url = creds["DB_URL"]
key = creds["PWD_DB"]

supa = create_client(url, key)

def add_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs["supabase"] = supa
        return func(*args, **kwargs)
    return wrapper
