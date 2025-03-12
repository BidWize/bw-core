from sqlmodel import Session, select
from app.entities.user import User
from fastapi import HTTPException


def get_all_users(db: Session):
    statement = select(User)
    results = db.exec(statement)
    return results.all()

def get_user_by_id(db: Session, user_id: int):
    return db.get(User, user_id)

def get_user_by_email(db: Session, email: str):
    statement = select(User).where(User.email == email)
    return db.exec(statement).first()

def get_user_by_username(db: Session, username: str):
    statement = select(User).where(User.username == username)
    return db.exec(statement).first()
    

def create_user(db: Session, user):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def search_users_in_db(db: Session, query: str):
    statement = select(User).where(
        (User.username.ilike(f"%{query}%")) | (User.email.ilike(f"%{query}%"))
    )
    results = db.exec(statement)
    return results.all()
    

def create_user_in_db(db: Session, user):
    # Check if username or email already exists
    if get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already taken")
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = User(
        username=user.username.lower(),  # Ensure case insensitivity
        email=user.email.lower(),  # Ensure case insensitivity
        password=user.password,
        is_active=True,
        is_admin=False,
        role=user.role,
        street=user.street,
        city=user.city,
        country=user.country,
        postal_code=user.postal_code
    )
    return create_user(db, db_user)

