#!/usr/bin/env python3

"""
This module provides authantication class
for handling authentication functionality.
"""

from typing import List, TypeVar
from flask import request


class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authantication is required for that path

        Arguments:
        path (str): The URL path to check
        for authentication requirements.
        excluded_paths (List[str]): A list of paths
        that are exempt from authentication.

        Returns:
        bool: Returns False
        for now (authentication is not required).
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrive authorization header from request

        Arguments:
        request: The Flask request object (optional).
        If not provided, defaults to None.

        Returns:
        str: The 'Authorization' header value,
        or None if no header is found.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder for the current user

        Arguments:
        request: The Flask request object (optional).
        If not provided, defaults to None.

        Returns:
        TypeVar('User'): Returns None for now
        but in the future, this will return the user object.
        """
        return None
