from sqlmodel import Session, select
from fastapi import HTTPException
from datetime import datetime
from app.entities.auction_ent import AuctionBase, BidBase
from app.models.auction_model import AuctionCreate, BidCreate

def get_all_auctions(db: Session):
    statement = select(AuctionBase)
    results = db.exec(statement)
    return results.all()

def get_auction_by_id(db: Session, auction_id: int):
    return db.get(AuctionBase, auction_id)

def create_auction(db: Session, auction_data: AuctionCreate):
    new_auction = AuctionBase(
        title=auction_data.title,
        description=auction_data.description,
        start_time=auction_data.start_time,
        end_time=auction_data.end_time,
    )
    db.add(new_auction)
    db.commit()
    db.refresh(new_auction)
    return new_auction

def place_bid(db: Session, auction_id: int, bid_data: BidCreate):
    auction = get_auction_by_id(db, auction_id)
    if not auction:
        return None
    if current_time := datetime.now() < auction.start_time:
        raise HTTPException(
            status_code=400,
            detail="Auction has not started yet",
        )
    if current_time > auction.end_time:
        raise HTTPException(
            status_code=400,
            detail="Auction has ended",
        )
    new_bid = BidBase(
        user_id=bid_data.user_id,
        amount=bid_data.amount,
        bidder=bid_data.bidder,
        bid_time=datetime.now(),
    )
    db.add(new_bid)
    db.commit()
    db.refresh(new_bid)
    return new_bid
