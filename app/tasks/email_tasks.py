from app.celery_app import app 
import time

@app.task(name='send_confirmation_email', queue='high')
def send_confirmation_email(email: str):
    """
    Task responsável por enviar email de confirmação.
    Executada pelo worker HIGH.
    """
    print(f"Sending confirmation email to {email}")
    time.sleep(10)
    # 1) Montar template
    # 2) Enviar email via SMTP / serviço externo
    # 3) Registrar logs
    print(f"Enviando email de confirmação para {email}")

    return {"status": "sent", "email": email}