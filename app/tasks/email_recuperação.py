from app.celery_app import app
from app.services.email_service import send_email


@app.task(name='send_recovery_email', queue='critical',
          bind=True, 
          max_retries=3,
          default_retry_delay=60)

def send_reset_email_task(self, email: str, reset_link: str):
    """
    Task responsável por enviar email de recuperação de senha.
    Executada pelo worker CRITICAL.
    """
    body = f"Clique no link para redefinir sua senha: {reset_link}"
    try:
        send_email(
            to_email=email,
            subject="Recuperação de Senha",
            body=body
        )
    except Exception as exc:
        print(f"Error sending password recovery email to {email}: {exc}")
        raise self.retry(exc=exc, countdown=60)  # Retry after 60 seconds
