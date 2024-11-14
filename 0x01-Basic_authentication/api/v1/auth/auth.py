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
        Check if authantication is required for the given path
        """
        if path is None:
            return True

        if excluded_paths is None:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrive authorization header from request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder for the current user
        """
        return None
