from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str
    email: str
    hashed_password: str
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True
        from_attributes = True

# Request model to create a new user.
class UserCreate(SQLModel):
    username: str
    email: str
    password: str

