from secrets import token_urlsafe
from hashlib import sha256
from datetime import datetime, timedelta


password_reset_tokens = {}


def create_reset_token(user_id: int):

    token = token_urlsafe(32)

    token_hash = sha256(
        token.encode()
    ).hexdigest()

    password_reset_tokens[token_hash] = {
        "user_id": user_id,
        "expires_at":
            datetime.utcnow() + timedelta(minutes=15),
        "used": False
    }

    return token


def validate_token(token: str):

    token_hash = sha256(
        token.encode()
    ).hexdigest()

    token_data = password_reset_tokens.get(
        token_hash
    )

    if not token_data:
        return None

    if token_data["used"]:
        return None

    if token_data["expires_at"] < datetime.utcnow():
        return None

    return token_data