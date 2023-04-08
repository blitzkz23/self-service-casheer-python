"""
This file contain Class for transaction to store transaction detail's of user
"""

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import relationship
from ..database.base import Base

class Transaction(Base):
    """
    A class for storing transaction detail including id, item_name, qty, price, total, disc, and after_disc

    Attributes:
        id (int): The unique identifier for the user.
        item_name (str): The name of the item.
        qty (int): The quantity of the item.
        price (float): The price of each item.
        total (float): The price of bought items.
        disc (int): Discount percentage after certain total threshold.
        after_disc (float): The total price after being discounted
    """

    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)
    item_name = Column(String(50), nullable=False)
    qty = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    disc = Column(Integer, nullable=False)
    after_disc = Column(Float, nullable=False)

    def __init__(self, user_id=None, item_name="", qty=0, price=0, total=0, disc=0, after_disc=0):
        self.user_id = user_id
        self.item_name = item_name
        self.qty = qty
        self.price = price
        self.total = total
        self.disc = disc
        self.after_disc = after_disc

    def __repr__(self):
        return f"<Transaction(id='{self.id}', user_id='{self.user_id}', item_name='{self.item_name}', qty={self.qty}, price={self.price}, total={self.total}, disc={self.disc}, after_disc={self.after_disc})>"

    