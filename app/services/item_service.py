from sqlmodel import Session, select
from fastapi import HTTPException
from app.entities.item_ent import Item
from app.models.item_model import ItemCreate

def get_all_items(db: Session):
    statement = select(Item)
    results = db.exec(statement)
    return results.all()

def get_item_by_id(db: Session, item_id: int):
    return db.get(Item, item_id)

def create_item(db: Session, item_data: ItemCreate):
    new_item = Item(
        name=item_data.name,
        description=item_data.description,
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_item(db: Session, item_id: int, item_data: ItemCreate):
    item = get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, item_id: int):
    item = get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"ok": True}