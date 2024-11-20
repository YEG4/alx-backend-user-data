#!/usr/bin/env python3
"""Hash module
"""

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """Hashes a password.
    """
    return hashpw(password.encode("utf-8"), gensalt())
