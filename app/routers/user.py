from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from app.models.models import UserCreate
from app.services.user_service import create_user
from app.services.user_service import banco, recover_password

router = APIRouter(tags=["users"], prefix="/users")

@router.get('/')
async def get_users():
    return {"message": "List of users", "users": banco}



@router.post('/new_user')
async def create_user_route(user: UserCreate):
    return create_user(name=user.name, email=user.email, password=user.password)


@router.post('/recuperar_senha')
async def recuperar_senha(email: str):

    
    # Aqui você chamaria a task Celery para enviar o email de recuperação de senha
    # Por exemplo: send_recovery_email.apply_async(args=[email], queue='critical')
    return recover_password(email=email)