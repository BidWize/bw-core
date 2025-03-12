from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
from fastapi import BackgroundTasks

from ..services.db import get_db
from ..services.auction_service import (
    determine_winner,
    process_ended_auctions,
    get_auction_with_winner
)
from ..entities.auction import Auction, AuctionCreate, AuctionRead, AuctionUpdate

router = APIRouter(
    prefix="/auctions",
    tags=["auctions"],
)


@router.post("/", response_model=AuctionRead, status_code=status.HTTP_201_CREATED)
def create_auction(auction: AuctionCreate, db: Session = Depends(get_db)):
    db_auction = Auction.model_validate(auction)
    db.add(db_auction)
    db.commit()
    db.refresh(db_auction)
    return db_auction


@router.get("/", response_model=List[AuctionRead])
def read_auctions(
    skip: int = 0, limit: int = 100, active_only: bool = False, db: Session = Depends(get_db)
):
    query = select(Auction)
    if active_only:
        query = query.where(Auction.is_active == True)
    
    auctions = db.exec(query.offset(skip).limit(limit)).all()
    return auctions


@router.get("/{auction_id}", response_model=AuctionRead)
def read_auction(auction_id: int, db: Session = Depends(get_db)):
    auction = db.get(Auction, auction_id)
    if not auction:
        raise HTTPException(status_code=404, detail="Auction not found")
    return auction


@router.patch("/{auction_id}", response_model=AuctionRead)
def update_auction(
    auction_id: int, auction_update: AuctionUpdate, db: Session = Depends(get_db)
):
    db_auction = db.get(Auction, auction_id)
    if not db_auction:
        raise HTTPException(status_code=404, detail="Auction not found")
    
    auction_data = auction_update.model_dump(exclude_unset=True)
    for key, value in auction_data.items():
        setattr(db_auction, key, value)
    
    db.add(db_auction)
    db.commit()
    db.refresh(db_auction)
    return db_auction


@router.delete("/{auction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_auction(auction_id: int, db: Session = Depends(get_db)):
    db_auction = db.get(Auction, auction_id)
    if not db_auction:
        raise HTTPException(status_code=404, detail="Auction not found")
    
    db.delete(db_auction)
    db.commit()
    return None


@router.get("/{auction_id}/status", response_model=dict)
def get_auction_status(auction_id: int, db: Session = Depends(get_db)):
    """Get detailed status of an auction, including winner information if ended"""
    result = get_auction_with_winner(db, auction_id)
    if not result:
        raise HTTPException(status_code=404, detail="Auction not found")
    return result


@router.post("/{auction_id}/end", response_model=dict)
def end_auction_manually(auction_id: int, db: Session = Depends(get_db)):
    """Manually end an auction and determine the winner"""
    auction = db.get(Auction, auction_id)
    if not auction:
        raise HTTPException(status_code=404, detail="Auction not found")
    
    if not auction.is_active:
        raise HTTPException(status_code=400, detail="Auction is already ended")
    
    winner = determine_winner(db, auction_id)
    
    if winner:
        return winner
    else:
        return {"message": "Auction ended, no bids were placed"}
    
@router.post("/process-ended", response_model=dict)
def process_ended_auctions_route(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
        """Process all auctions that have ended"""
        count = process_ended_auctions(db)
        return {"message": f"Processed {count} ended auctions"}