#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError, NoResultFound
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
        email = kwargs['email']
        if kwargs['email'] == "" or None:
            raise InvalidRequestError()

        user = self.__session.query().filter(
            User.email == kwargs['email']).first()
        if user is not None:
            return user
        else:
            raise NoResultFound
