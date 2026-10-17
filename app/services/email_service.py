import smtplib
from email.mime.text import MIMEText

from app.settings import settings


def send_email(to_email: str, subject: str, body: str):

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = settings.SMTP_FROM
    msg["To"] = to_email

    with smtplib.SMTP(
        settings.SMTP_HOST,
        settings.SMTP_PORT
    ) as smtp:
        smtp.send_message(msg)
