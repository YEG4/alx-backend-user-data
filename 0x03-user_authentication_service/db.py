#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """this method adds a new user to the database

        Args:
            email (string): email of the user.
            hashed_password (string): password to be saved in the db.

        Returns:
            user: A user object.
        """
        try:
            user = User(email=email, hashed_password=hashed_password)
            session = self._session
            session.add(user)
            session.commit()
        except Exception:
            session.rollback()
            user = None

        return user

    def find_user_by(self, **kwargs) -> User:
        """This method returns a user for a given condition
        """
        fields, values = [], []

        for key, value in kwargs.items():
            if hasattr(User, key):
                fields.append(getattr(User, key))
                values.append(value)
            else:
                raise InvalidRequestError()

        user = self.__session.query(User).filter(
            tuple_(*fields).in_([tuple(values)])).first()
        if user is None:
            raise NoResultFound()
        return user

    def update_user(self, userId: int, **kwargs) -> None:
        user = self.find_user_by(id=userId)
        if user is None:
            return None
        for key, value in kwargs.items():
            if hasattr(User, key):
                setattr(user, key, value)
            else:
                raise ValueError()
