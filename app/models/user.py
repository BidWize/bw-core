from pydantic import BaseModel

# Request model to create a new user.
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Response model for a user.
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

# Request model to authenticate a user.
class UserAuthenticate(BaseModel):
    username: str
    password: str

# Request model to update a user.
class UserUpdate(BaseModel):
    username: str
    email: str
