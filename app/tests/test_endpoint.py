from fastapi.testclient import TestClient

from app.main import api

client = TestClient(api)

def test_forgot_password_endpoint():

    response = client.post(
        "/users/forgot-password",
        json={
            "email": "teste@email.com"
        }
    )

    assert response.status_code == 200