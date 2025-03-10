from sqlmodel import Session, select
from app.entities.user import User

def get_all_users(db: Session):
    statement = select(User)
    results = db.exec(statement)
    return results.all()

def get_user_by_id(db: Session, user_id: int):
    return db.get(User, user_id)

def get_user_by_email(db: Session, email: str):
    statement = select(User).where(User.email == email)
    return db.exec(statement).first()

def create_user(db: Session, user):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_user_in_db(db: Session, user):
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=user.password,
        is_active=True,
        is_admin=False
    )
    return create_user(db, db_user)
