from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# Response model for a bid.
class BidResponse(BaseModel):
    id: int
    amount: float
    bidder: str
    bid_time: datetime

    class Config:
        from_attributes = True

# Response model for an auction. Includes a list of bids.
class AuctionResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    bids: List[BidResponse] = []

    class Config:
        from_attributes = True

# Request model to create a new auction.
class AuctionCreate(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime

# Request model to create a new bid.
class BidCreate(BaseModel):
    amount: float
    bidder: str
