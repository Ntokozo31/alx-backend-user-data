#!/usr/bin/env python3

"""
This module provides authantication class
"""

from flask import request
from typing import List, TypeVar


class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authantication is required for that path"""
        return False

    def authorization_header(self, request=None) -> str:
        """Retrive authorization header from request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Placeholder for the current user"""
        return None
