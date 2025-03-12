from pydantic import BaseModel
from app.entities.user import UserRole  # Import the role enum
from typing import Optional

# Request model to create a new user.
class UserCreate(BaseModel):
    username: str
    email: str
    password: str  # Plain text for now
    role: UserRole  # Choose 'buyer' or 'seller'
    street: str
    city: str
    country: str
    postal_code: str

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
    username: Optional[str] = None
    email: Optional[str] = None
    role: Optional[UserRole] = None
    street: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
