#!/usr/bin/env python3
"""This file contains User Table.
"""

from sqlalchemy import Column, Integer, String
from base import Base


class User(Base):
    """This Class represents a table in the database called users

    Args:
        Base (declarative_base): declarative base class
        that maintains or contains metadata about tables relative to that base.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
