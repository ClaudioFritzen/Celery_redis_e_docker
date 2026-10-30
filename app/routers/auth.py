from fastapi import APIRouter, HTTPException
from http import HTTPStatus
from app.schema.forgor_password import ForgotPasswordRequest, ResetPasswordRequest
from app.services.user_service import recover_password
from app.services.user_service import banco
from app.services.password_reset_service import validate_token, password_reset_tokens
from hashlib import sha256

router = APIRouter(tags=["auth"], prefix="/auth")


@router.post('/forgot-password')
async def forgot_password(payload: ForgotPasswordRequest):
 
    return recover_password(payload.email)


@router.post('/reset-password')
async def reset_password(payload: ResetPasswordRequest):

    token_data = validate_token(
        payload.token
    )
    if not token_data:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                             detail="Invalid or expired token")


    user_id = token_data['user_id']

    user = next(
        (user for user in banco if user['id'] == user_id),
        None
    )

    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                             detail="User not found")

    user['password'] = payload.new_password

    token_hash = sha256(
        payload.token.encode()
    ).hexdigest()

    password_reset_tokens[token_hash]['used'] = True

    return {"message": "Password reset successful"}