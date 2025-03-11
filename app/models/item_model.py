from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# Request model to create a new item
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None

# Response model for an item
class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    
    class Config:
        from_attributes = True

# Update model for an item
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

# Remove item model
class ItemRemove(BaseModel):
    id: int