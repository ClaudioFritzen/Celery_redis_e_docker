from app.tasks.email_tasks import send_confirmation_email
from app.tasks.email_recuperação import send_reset_email_task
from app.services.password_reset_service import create_reset_token, validate_token


banco = []  # Simulando um banco de dados em memória

def create_user(name: str, email: str, password: str):

    # aqui salvamos no banco
    user = {"id": len(banco) + 1, "name": name, "email": email, "password": password}
    banco.append(user)

    # chamamos a task Celery para enviar o email de confirmação
    send_confirmation_email.apply_async(args=[email], queue='high')
    return f'User created successfully! Check your email {email} to verify your account.'


def recover_password(email: str):
    # Aqui você implementaria a lógica para recuperar a senha
    # Por exemplo, você poderia gerar um token de recuperação e enviá-lo por email
    print(f"[DEBUG] recover_password chamado para {email}")
    user = next((user for user in banco if user['email'] == email), None)
        
    if not user:
        print("[DEBUG] Usuário não encontrado")
        return {"message": f"Password recovery email sent to {email}"}
    print(f"[DEBUG] Usuário encontrado: {user}")

    token = create_reset_token(user_id=user['id'])
    print(f"[DEBUG] Token criado: {token}")

    reset_link = f"http://localhost:8000/auth/reset-password?token={token}"
    print("[DEBUG] Enviando task para Celery")
    print(f"[DEBUG] Password recovery link for {email}: {reset_link}")

    # dispara a task Celery para enviar o email de recuperação de senha
    send_reset_email_task.apply_async(args=[email, reset_link], queue='critical')
    return {
        "message":
        "If the email exists, recovery instructions were sent. Please check your email for further instructions."
    }

