from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.models.user import UserResponse, UserUpdate
from app.services.user import *
from app.services.db import get_db
from app.models.user import UserCreate

router = APIRouter(prefix="/user", tags=["User Management"])

@router.get("/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
@router.get("/search/", response_model=List[UserResponse])
def search_users(query: str, db: Session = Depends(get_db)):
    users = search_users_in_db(db, query)
    return users


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user_in_db(db, user)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Prevent duplicate email updates
    if user_update.email and user_update.email.lower() != user.email.lower():
        existing_user = get_user_by_email(db, user_update.email.lower())
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

    # Update only provided fields
    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(user, field, value.lower() if field in ["username", "email"] else value)

    db.commit()
    db.refresh(user)
    return user



@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return user
