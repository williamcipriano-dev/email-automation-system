import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email():
    try:
        msg = EmailMessage()

        msg["Subject"] = "Teste de Automação"
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_USER

        msg.set_content(
            "Este é um email enviado automaticamente pelo sistema em Python."
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("Email enviado com sucesso!")

    except Exception as error:
        print(f"Erro ao enviar email: {error}")