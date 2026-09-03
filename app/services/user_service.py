from app.tasks.email_tasks import send_confirmation_email
from app.tasks.email_recuperação import send_recovery_email


banco = []  # Simulando um banco de dados em memória

def create_user(name: str, email: str, password: str):

    # aqui salvamos no banco
    user = {"name": name, "email": email, "password": password}
    banco.append(user)

    # chamamos a task Celery para enviar o email de confirmação
    send_confirmation_email.apply_async(args=[email], queue='high')
    return f'User created successfully! Check your email {email} to verify your account.'


def recover_password(email: str):
    # Aqui você implementaria a lógica para recuperar a senha
    # Por exemplo, você poderia gerar um token de recuperação e enviá-lo por email

    email_exists = any(user['email'] == email for user in banco)

    if not email_exists:
        ## seguranda LGPD
        return {"message": f"Password recovery email sent to {email}"}

    # dispara a task Celery para enviar o email de recuperação de senha
    send_recovery_email.apply_async(args=[email], queue='critical')
    return f'Password recovery email sent to {email}'

