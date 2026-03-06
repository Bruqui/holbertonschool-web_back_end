#!/usr/bin/env python3
"""
Module DB pour gérer les interactions avec la base de données.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User


class DB:
    """
    Classe DB gérant la connexion et les opérations sur la base de données.
    """

    def __init__(self) -> None:
        """
        Initialise une nouvelle instance de la base de données.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Objet session mémorisé (memoized) pour les requêtes SQLAlchemy.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Ajoute un nouvel utilisateur à la base de données.

        Args:
            email (str): L'email de l'utilisateur.
            hashed_password (str): Le mot de passe haché de l'utilisateur.

        Returns:
            User: L'objet User nouvellement créé.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user
