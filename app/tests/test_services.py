from unittest.mock import MagicMock
from app.services.user_service import create_user
import app.services.user_service as user_service


def test_create_user_calls_celery(monkeypatch):
    mock_apply_async = MagicMock()
    monkeypatch.setattr(
        user_service.send_confirmation_email,
        "apply_async",
        mock_apply_async
    )

    

    email = "claudio@example.com"
    create_user("Claudio", email, "123")
    


    mock_apply_async.assert_called_once_with(
        args=[email],
        queue="high"
    )
