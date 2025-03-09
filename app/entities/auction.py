from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

# Base class for common auction properties
class AuctionBase(SQLModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime

# Auction is a table with a primary key and a relationship to bids.
class Auction(AuctionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    bids: List["Bid"] = Relationship(back_populates="auction")

# Base class for bid information
class BidBase(SQLModel):
    amount: float

# Bid table with a foreign key referencing Auction.
class Bid(BidBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    auction_id: int = Field(foreign_key="auction.id")
    bidder: str
    bid_time: datetime
    auction: Optional[Auction] = Relationship(back_populates="bids")
