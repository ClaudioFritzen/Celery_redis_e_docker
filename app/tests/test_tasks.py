from app.tasks.email_tasks import send_confirmation_email


def test_send_confirmation_email():
    result = send_confirmation_email("claudio@example.com")

    assert result["status"] == "sent"
    assert result["email"] == "claudio@example.com"



def test_task_queue():
    assert send_confirmation_email.queue == "high"
