from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.models.item_model import ItemResponse, ItemCreate
from app.entities.item_ent import Item
from app.services.item_service import (
    get_all_items,
    get_item_by_id,
    create_item,
    update_item,
    delete_item,
)
from app.services.db import get_db

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/", response_model=List[ItemResponse])
def list_items(db: Session = Depends(get_db)):
    items = get_all_items(db)
    return items

@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=ItemResponse, status_code=201)
def create_new_item(
    item_data: ItemCreate, db: Session = Depends(get_db)
):
    item = create_item(db, item_data)
    return item

@router.put("/{item_id}", response_model=ItemResponse)
def update_existing_item(
    item_id: int, item_data: ItemCreate, db: Session = Depends(get_db)
):
    updated_item = update_item(db, item_id, item_data)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/{item_id}")
def delete_existing_item(item_id: int, db: Session = Depends(get_db)):
    result = delete_item(db, item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item successfully deleted"}