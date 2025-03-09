from sqlmodel import Session, select
from datetime import datetime
from app.entities.auction import Auction, Bid
from app.models.auction import AuctionCreate, BidCreate

def get_all_auctions(db: Session):
    statement = select(Auction)
    results = db.exec(statement)
    return results.all()

def get_auction_by_id(db: Session, auction_id: int):
    return db.get(Auction, auction_id)

def create_auction(db: Session, auction_data: AuctionCreate):
    new_auction = Auction(
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
    new_bid = Bid(
        amount=bid_data.amount,
        bidder=bid_data.bidder,
        bid_time=datetime.utcnow(),
        auction_id=auction_id,
    )
    db.add(new_bid)
    db.commit()
    db.refresh(new_bid)
    return new_bid
