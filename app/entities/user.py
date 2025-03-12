from sqlmodel import Field, SQLModel
from enum import Enum

class UserRole(str, Enum):
    BUYER = "buyer"
    SELLER = "seller"

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str = Field(unique=True, index=True)  # Enforce unique username
    email: str = Field(unique=True, index=True)  # Enforce unique email
    password: str
    is_active: bool
    is_admin: bool
    role: UserRole
    street: str
    city: str
    country: str
    postal_code: str



    class Config:
        orm_mode = True
        from_attributes = True

# Request model to create a new user.
class UserCreate(SQLModel):
    username: str
    email: str
    password: str  # Plain text for now
    role: UserRole  # Choose 'buyer' or 'seller'
    street: str
    city: str
    country: str
    postal_code: str


