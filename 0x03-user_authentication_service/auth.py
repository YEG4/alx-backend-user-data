from bcrypt import hashpw, gensalt


def _hash_password(hashed_password: str) -> bytes:
    bytes = hashed_password.encode('utf-8')
    salt = gensalt()
    return hashpw(bytes, salt)
