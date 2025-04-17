from fastapi import APIRouter, Depends, Response
from schemas.user_schema import UserResponse, UserData, UserOut
from deps.db_deps import get_db
from models.user_model import User
from sqlalchemy.orm import Session
from utils.token_generators import generate_access_token, generate_refresh_token
from utils.password_utils import password_hash

router = APIRouter()


@router.post("/register", response_model=UserResponse, tags=["v1", "User"])
def register_router(user: UserData, response: Response, db: Session = Depends(get_db)):

    new_user = User(first_name=user.first_name, last_name=user.last_name, username=user.username, email=user.email, password=password_hash(user.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    user_dict = UserOut.from_orm(new_user).dict()

    ACCESS_TOKEN = generate_access_token(user_dict)
    REFRESH_TOKEN = generate_refresh_token(user_dict)

    response.set_cookie(key="ACCESS_TOKEN", value=ACCESS_TOKEN, httponly=True, secure=True)
    response.set_cookie(key='REFRESH_TOKEN', value=REFRESH_TOKEN, httponly=True, secure=True)

    return {"status_code": 201, "message": "User created", "data": new_user, "success": True}
