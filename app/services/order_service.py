from sqlalchemy.orm import Session
from app.models.order import Order as OrderModel
from app.models.user import User as UserModel
from app.schemas.order import OrderRequest
from app.services.auction_service import get_auction_with_winner
from app.services.user_service import get_user_by_id
from fastapi import HTTPException

class OrderService:
    @staticmethod
    def get_order(db: Session, auction_id: int) -> OrderRequest:
        # Step 1: Get the auction details including the winning user ID
        auction_data = get_auction_with_winner(db, auction_id)
        if not auction_data or "winner" not in auction_data:
            raise HTTPException(status_code=404, detail="No winner found for this auction")

        winner_user_id = auction_data["winner"]["user_id"]

        # Step 2: Retrieve the user information based on the winning user ID
        user = get_user_by_id(db, winner_user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Winner user not found")

        # Step 3: Retrieve the order related to this auction
        order = (
            db.query(OrderModel)
            .filter(OrderModel.item_id == auction_data["item"]["id"])
            .first()
        )
        
        if not order:
            raise HTTPException(status_code=404, detail="Order not found for this auction's item")

        # Step 4: Return the formatted order details
        order_response = OrderRequest(
            user_name=user.username,
            street_address=user.street,
            phone_number=order.phone_number,
            province=order.province,
            country=user.country,
            postal_code=user.postal_code,
            total_paid=order.total_paid,
            item_id=order.item_id
        )

        return order_response
