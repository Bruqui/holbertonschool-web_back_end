#!/usr/bin/env python3
"""
Module d'authentification pour gérer la sécurité des mots de passe.
"""
import bcrypt


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
