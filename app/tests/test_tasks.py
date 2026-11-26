from unittest.mock import patch
from app.tasks.email_tasks import send_confirmation_email

@patch("app.tasks.email_tasks.send_email")
def test_send_confirmation_email(mock_send_email):

    result = send_confirmation_email(
        "claudio@example.com",
        "http://localhost:8000/auth/verify-email?token=abc123"
        )

    mock_send_email.assert_called_once()
    

    assert result["status"] == "sent"
    assert result["email"] == "claudio@example.com"



def test_task_queue():
    assert send_confirmation_email.queue == "high"
