from app.celery_app import app 
from app.services.email_service import send_email

@app.task(
        name='send_confirmation_email',
        queue='high',
        bind=True, #mesmo que self, permite acessar o contexto da task
        max_retries=3,
        default_retry_delay=60
    )
def send_confirmation_email(self, email: str, verify_link: str):
    """
    Task responsável por enviar email de confirmação.
    Executada pelo worker HIGH.
    """

    body = f"""
        Olá, por favor clique no link abaixo para verificar seu email:
        {verify_link}
    """

    try:
        

        send_email(
            to_email=email,
            subject="Confirmação de Email",
            body=body
        )
        return {"status": "sent", "email": email}
    
    except Exception as e:
        print(f"Erro ao enviar email para {email}: {e}")

        raise self.retry(
            exc=e,
            countdown=60)

    