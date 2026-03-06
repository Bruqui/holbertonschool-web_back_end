#!/usr/bin/env python3
"""
Module d'authentification pour gérer la sécurité des mots de passe
et les opérations sur les utilisateurs.
"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hache un mot de passe en utilisant bcrypt.

    Args:
        password (str): Le mot de passe en clair à hacher.

    Returns:
        bytes: Le mot de passe haché et salé.
    """
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt)


def _generate_uuid() -> str:
    """
    Génère une nouvelle représentation sous forme de chaîne d'un UUID.

    Returns:
        str: Un UUID généré aléatoirement.
    """
    return str(uuid.uuid4())


class Auth:
    """
    Classe Auth gérant l'authentification et l'interaction
    avec la base de données.
    """

    def __init__(self) -> None:
        """
        Initialise une nouvelle instance Auth avec une connexion DB.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Enregistre un nouvel utilisateur s'il n'existe pas déjà.

        Args:
            email (str): L'email de l'utilisateur.
            password (str): Le mot de passe en clair.

        Returns:
            User: L'objet User nouvellement créé.

        Raises:
            ValueError: Si l'utilisateur existe déjà avec cet email.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            return self._db.add_user(email, hashed_pwd)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Vérifie si les identifiants de connexion sont valides.

        Args:
            email (str): L'email de l'utilisateur.
            password (str): Le mot de passe en clair à vérifier.

        Returns:
            bool: True si les identifiants sont corrects, False sinon.
        """
        try:
            user = self._db.find_user_by(email=email)

            pwd_bytes = password.encode('utf-8')

            hashed_bytes = (
                user.hashed_password.encode('utf-8')
                if isinstance(user.hashed_password, str)
                else user.hashed_password
            )

            return bcrypt.checkpw(pwd_bytes, hashed_bytes)

        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Crée une nouvelle session pour l'utilisateur.

        Args:
            email (str): L'email de l'utilisateur.

        Returns:
            str: L'ID de session généré, ou None si l'utilisateur n'existe pas.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return session_id
