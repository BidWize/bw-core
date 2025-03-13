from sqlalchemy.orm import Session
from app.entities.paymentmethod import PaymentMethod

class PaymentVerificationService:
    @staticmethod
    def verify_payment_info(db: Session, card_number: str, card_holder_name: str, expiry_date: str, security_code: str) -> bool:
        return db.query(PaymentMethod).filter_by(
            card_number=card_number,
            card_holder_name=card_holder_name,
            expiry_date=expiry_date,
            security_code=security_code
        ).first() is not None
