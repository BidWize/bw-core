from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.order_service import OrderService
from app.services.db import get_db

router = APIRouter()

@router.get("/orders/auction/{auction_id}")
def get_order_by_auction(auction_id: int, db: Session = Depends(get_db)):
    try:
        return OrderService.get_order(db, auction_id)
    except HTTPException as e:
        raise e
