from jose import JWTError, jwt
from datetime import timedelta, datetime


def generate_access_token(user: dict):
    to_encode = user.copy()
    expires = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expires})

    return jwt.encode(to_encode, "SECRETORY", algorithm="HS256")

def generate_refresh_token(user: dict):
    to_encode = user.copy()
    expires = datetime.utcnow() + timedelta(days=30)
    to_encode.update({"exp": expires})

    return jwt.encode(to_encode, "SECRETORY", algorithm="HS256")