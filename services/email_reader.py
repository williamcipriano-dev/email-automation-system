from imap_tools import MailBox
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def read_emails():
    try:
        with MailBox("imap.gmail.com").login(
            EMAIL_USER,
            EMAIL_PASSWORD,
            "INBOX"
        ) as mailbox:

            print("\nEmails encontrados:\n")

            for msg in mailbox.fetch(limit=10, reverse=True):

                category = "Outros"

                sender = msg.from_.lower()
                subject = msg.subject.lower()

                if "indeed" in sender:
                    category = "Oportunidade de Trabalho"

                elif "pinterest" in sender:
                    category = "Promocional"

                elif "hashtag" in sender:
                    category = "Estudos"

                elif "vaga" in subject:
                    category = "Possível Vaga"

                print(f"Categoria: {category}")
                print(f"Remetente: {msg.from_}")
                print(f"Assunto: {msg.subject}")
                print(f"Data: {msg.date}")
                print("-" * 50)

    except Exception as error:
        print(f"Erro ao ler emails: {error}")