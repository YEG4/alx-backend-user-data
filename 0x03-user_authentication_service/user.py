#!/usr/bin/env python3
"""This file contains User Table.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """This Class represents a table in the database called users

    Args:
        Base (declarative_base): declarative base class
        that maintains or contains metadata about tables relative to that base.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
