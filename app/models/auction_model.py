from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# Request model to create a new bid.
class BidCreate(BaseModel):
    amount: float
    bidder: str
    user_id: int

# Response model for a bid.
class BidResponse(BaseModel):
    id: int
    amount: float
    bidder: str
    bid_time: datetime

    class Config:
        from_attributes = True

# Update model for a bid.
class BidUpdate(BaseModel):
    amount: Optional[float] = None
    bidder: Optional[str] = None

# Remove bid model.
class BidRemove(BaseModel):
    id: int

# Request model to create a new auction.
class AuctionCreate(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime

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

# Update model for an auction.
class AuctionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[
        datetime
    ] = None

# Remove auction model.
class AuctionRemove(BaseModel):
    id: int


