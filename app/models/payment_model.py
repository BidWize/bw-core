from pydantic import BaseModel
from typing import Optional

# Base model for payment method creation (request schema)
class PaymentMethodBase(BaseModel):
    card_number: str  # The credit card number (should be encrypted in production)
    card_holder_name: str  # The cardholder's name
    expiry_date: str  # The expiration date of the card in MM/YY format
    security_code: str  # The security code (CVV) of the card (should be encrypted in production)

    class Config:
        orm_mode = True  # Allows compatibility with ORM models (like SQLAlchemy)

# Response model for payment method (returned data after creation)
class PaymentMethodResponse(PaymentMethodBase):
    id: int  # The ID of the payment method (from the database)
    user_id: int  # The ID of the user associated with this payment method

    class Config:
        orm_mode = True  # Allows compatibility with ORM models (like SQLAlchemy)
