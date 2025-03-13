from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    last_four_digits = Column(String(4), nullable=False)
    card_brand = Column(String, nullable=False)
    payment_status = Column(String, nullable=False)

    def __repr__(self):
        return f"<PaymentMethod transaction_id={self.transaction_id} status={self.payment_status}>"