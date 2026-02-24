#!/usr/bin/env python3
"""
Module for encrypting passwords securely using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password using bcrypt.
    """
    # bcrypt a besoin de bytes, on doit donc encoder le string en utf-8
    encoded_password = password.encode('utf-8')
    # gensalt() génère un sel unique pour chaque mot de passe
    salt = bcrypt.gensalt()
    
    return bcrypt.hashpw(encoded_password, salt)
