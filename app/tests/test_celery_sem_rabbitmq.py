from unittest.mock import patch

from app.tasks.email_recuperação import (
    send_reset_email_task
)

@patch(
    "app.tasks.email_recuperação.send_email"
)
def test_send_reset_email(
    mock_send_email
):

    send_reset_email_task.run(
        "teste@email.com",
        "http://teste.com"
    )

    mock_send_email.assert_called_once()

    mock_send_email.assert_called_with(
        to_email="teste@email.com",
        subject="Recuperação de Senha",
        body="Clique no link para redefinir sua senha: http://teste.com"
    )

from unittest.mock import patch

from app.tasks.email_recuperação import send_reset_email_task


@patch("app.tasks.email_recuperação.send_email")
def test_send_reset_email_task(mock_send_email):

    send_reset_email_task.run(
        "teste@email.com",
        "http://teste.com"
    )

    mock_send_email.assert_called_once()
