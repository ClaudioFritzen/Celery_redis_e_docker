
from fastapi import APIRouter
from app.models.models import UserCreate
from app.services.email_service import send_email
from app.services.user_service import create_user
from app.services.user_service import banco

router = APIRouter(tags=["users"], prefix="/users")

@router.get('/')
async def get_users():
    return {"message": "List of users", "users": banco}



@router.post('/new_user')
async def create_user_route(user: UserCreate):
    return create_user(name=user.name, email=user.email, password=user.password)


@router.get("/test-email")
def test_email():

    send_email(
        to_email="teste@email.com",
        subject="SMTP funcionando",
        body="Olá mundo"
    )

    return {"status": "email enviado"}