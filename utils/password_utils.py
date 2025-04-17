from passlib.context import CryptContext

pwd_context = CryptContext(schemes="bcrypt", deprecated="auto")

def password_hash(password):

    return pwd_context.hash(password)

def password_verify(plain, hashed):

    return pwd_context.verify(plain, hashed)