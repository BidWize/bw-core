from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class AuctionBase(SQLModel):
    start_date: datetime
    end_date: datetime
    min_bid_increment: float = 1.0
    item_id: int = Field(foreign_key="item.id")


class Auction(AuctionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    item: "Item" = Relationship(back_populates="auctions")
    bids: List["Bid"] = Relationship(back_populates="auction")


class AuctionCreate(AuctionBase):
    pass


class AuctionRead(AuctionBase):
    id: int
    is_active: bool
    created_at: datetime


class AuctionUpdate(SQLModel):
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    min_bid_increment: Optional[float] = None
    is_active: Optional[bool] = None
