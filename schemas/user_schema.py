from pydantic import BaseModel

class UserOut(BaseModel):

    id: int
    first_name: str
    last_name: str
    username: str

    model_config = {
        "from_attributes": True
    }

class UserData(BaseModel):

    first_name: str
    last_name: str
    username: str
    email: str
    password: str

class UserResponse(BaseModel):

    status_code: int = 200
    data: UserOut
    message: str = "ok"
    success: bool = True
