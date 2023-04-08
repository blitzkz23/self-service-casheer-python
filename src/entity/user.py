"""
This file contain Class for User to store email, name, and password.
"""

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from ..database.base import Base

class User(Base):
    """
    A class for storing user information, including email, name, and password.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The password for the user's account.
    """

    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(50), nullable=False)
    password = Column(String(25), nullable=False)

    def __init__(self, email="", name="", password=""):
        self.email = email
        self.name = name
        self.password = password

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

    def welcome_user(self):
        return f'--- Selamat datang, {self.name}! ---'
    