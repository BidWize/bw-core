from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.models.auction import AuctionResponse, AuctionCreate, BidCreate, BidResponse
from app.entities.auction import Auction, Bid
from app.services.auction import (
    get_all_auctions,
    get_auction_by_id,
    create_auction,
    place_bid,
)
from app.services.db import get_db

router = APIRouter(prefix="/auctions", tags=["Auctions"])

@router.get("/", response_model=List[AuctionResponse])
def list_auctions(db: Session = Depends(get_db)):
    auctions = get_all_auctions(db)
    return auctions

@router.get("/{auction_id}", response_model=AuctionResponse)
def read_auction(auction_id: int, db: Session = Depends(get_db)):
    auction = get_auction_by_id(db, auction_id)
    if not auction:
        raise HTTPException(status_code=404, detail="Auction not found")
    return auction

@router.post("/", response_model=AuctionResponse, status_code=201)
def create_new_auction(
    auction_data: AuctionCreate, db: Session = Depends(get_db)
):
    auction = create_auction(db, auction_data)
    return auction

@router.post("/{auction_id}/bids", response_model=BidResponse, status_code=201)
def add_bid(
    auction_id: int, bid_data: BidCreate, db: Session = Depends(get_db)
):
    new_bid = place_bid(db, auction_id, bid_data)
    if new_bid is None:
        raise HTTPException(status_code=404, detail="Auction not found")
    return new_bid
