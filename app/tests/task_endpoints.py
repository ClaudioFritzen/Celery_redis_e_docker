from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import api
import app.services.user_service as user_service

client = TestClient(api)


def test_new_user_endpoint(monkeypatch):
    mock_apply_async = MagicMock()
    monkeypatch.setattr(
        user_service.send_confirmation_email,
        "apply_async",
        mock_apply_async
    )

    payload = {
        "name": "Claudio",
        "email": "claudio@example.com",
        "password": "123"
    }

    response = client.post("/new_user", json=payload)

    breakpoint()

    assert response.status_code == 200
    assert "User created successfully" in response.text

    mock_apply_async.assert_called_once()
