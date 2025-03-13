from app.entities.payment import Payment
#from app.models.payment import Payment as PaymentModel
from sqlalchemy.orm import Session
from app.models.payment_model import PaymentRequest

class PaymentService:
    @staticmethod
    def process_payment(db: Session, payment_data: PaymentRequest):
        # Example logic for processing payment
        payment = PaymentRequest(
            card_number=payment_data.card_number,
            card_holder_name=payment_data.card_holder_name,
            expiry_date=payment_data.expiry_date,
            security_code=payment_data.security_code
        )

        # Save to database
        db.add(payment)
        db.commit()
        db.refresh(payment)

        return {"message": "Payment processed successfully", "payment_id": payment.id}
