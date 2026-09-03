"""
Nesse arquivo, vamos adicionar a lógica para enviar e-mails de recuperação de senha
para os usuários que esqueceram suas senhas. A função principal será responsável por gerar um token de recuperação, 
criar o conteúdo do e-mail e enviar o e-mail para o usuário.    

"""

from app.celery_app import app 

@app.task(name='send_recovery_email', queue='critical')
def send_recovery_email(email: str):
    """
    Task responsável por enviar email de recuperação de senha.
    Executada pelo worker CRITICAL.
    """
    print(f"Sending password recovery email to {email}")
    # Aqui você implementaria a lógica para enviar o e-mail de recuperação de senha
    # Por exemplo, você poderia gerar um token de recuperação e enviá-lo por e-mail
    return {"status": "sent", "email": email}