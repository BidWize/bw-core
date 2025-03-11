from __future__ import annotations
from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class AuctionBase(SQLModel):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime

    bids: List["BidBase"] = Relationship(back_populates="auction")

class BidBase(SQLModel):
    user_id: int
    bidder: str
    amount: float
    bid_time: datetime
   