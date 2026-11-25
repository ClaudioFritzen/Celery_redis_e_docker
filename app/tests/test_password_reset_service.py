from app.services.password_reset_service import (
    create_reset_token,
    validate_token,
    password_reset_tokens
)

from datetime import datetime, timedelta
from hashlib import sha256





def test_create_token():

    token = create_reset_token(user_id=1)

    assert token is not None

    token_data = validate_token(token)

    assert token_data is not None
    assert token_data["user_id"] == 1
    assert token_data["used"] is False


def test_validate_token_invalid():

    invalid_token = "invalidtoken"
    token_data = validate_token(invalid_token)

    assert token_data is None   


def test_expired_token():

    token = 'token_fake'

    token_hash = sha256(
        token.encode('utf-8')
    ).hexdigest()

    print(f"Token hash: {token_hash}")
    password_reset_tokens[token_hash] = {
        'user_id': 1,
        'expires_at': datetime.utcnow() - timedelta(minutes=1),
        'used': False

    }

    assert validate_token(token) is None