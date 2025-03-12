from pydantic import BaseModel

# Pydantic model for Payment request
class PaymentRequest(BaseModel):
    card_number: str  # The card number provided by the user
    card_holder_name: str  # The name on the card
    expiry_date: str  # Expiry date of the card (e.g., 'MM/YY')
    security_code: str  # The card's security code (CVV)

    class Config:
        orm_mode = True
