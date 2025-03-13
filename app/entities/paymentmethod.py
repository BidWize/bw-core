from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key to User
    card_number = Column(String, nullable=False)
    card_holder_name = Column(String, nullable=False)
    expiry_date = Column(String, nullable=False)
    security_code = Column(String, nullable=False)  # This should be encrypted

    # Define the relationship to the User table
    user = relationship("User", back_populates="payment_methods")  # Relationship to User

    def __repr__(self):
        return f"<PaymentMethod id={self.id} user_id={self.user_id}>"

