class PaymentInfo(Base):
    __tablename__ = "payment_info"

    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String, nullable=False)
    card_holder_name = Column(String, nullable=False)
    expiry_date = Column(String, nullable=False)
    security_code = Column(String, nullable=False)
