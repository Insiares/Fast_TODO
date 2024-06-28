import yaml
from supabase import create_client
from functools import wraps



''' def add_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs["supabase"] = supa
        return func(*args, **kwargs)
    return wrapper
 '''