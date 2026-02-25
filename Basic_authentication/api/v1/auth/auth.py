#!/usr/bin/env python3
"""
Module to manage the API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template class for all authentication systems.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from a request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user from a request.
        """
        return None
