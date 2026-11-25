from unittest.mock import patch

from app.services.user_service import (
    banco,
    recover_password,
)

@patch(
    "app.services.user_service.send_reset_email_task"
)
def test_recover_password(mock_task):

    banco.clear()

    banco.append(
        {
            "id": 1,
            "email": "teste@email.com",
            "password": "123"
        }
    )

    recover_password("teste@email.com")

    mock_task.apply_async.assert_called_once()

    args, kwargs = mock_task.apply_async.call_args

    assert kwargs["queue"] == "critical"

    assert kwargs["args"][0] == "teste@email.com"

def test_email_not_found():

    banco.clear()

    response = recover_password(
        "naoexiste@email.com",
    )

    assert response == {
        "message":
        "Password recovery email sent to naoexiste@email.com"
    }