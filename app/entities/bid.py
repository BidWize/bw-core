from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime


class BidBase(SQLModel):
    amount: float
    bidder_name: str
    bidder_email: str
    auction_id: int = Field(foreign_key="auction.id")


class Bid(BidBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    
    # Relationships
    auction: "Auction" = Relationship(back_populates="bids")


class BidCreate(BidBase):
    pass


class BidRead(BidBase):
    id: int
    created_at: datetime


class BidUpdate(SQLModel):
    amount: Optional[float] = None
    bidder_name: Optional[str] = None
    bidder_email: Optional[str] = None
