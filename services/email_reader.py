from datetime import datetime
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

            with open(
                "logs/email_logs.txt",
                "a",
                encoding="utf-8"
            ) as log_file:

                for msg in mailbox.fetch(limit=10, reverse=True):

                    category = "Outros"

                    sender = msg.from_.lower()
                    subject = msg.subject.lower()

                    # FILTROS INTELIGENTES

                    if "indeed" in sender:
                        category = "Oportunidade de Trabalho"

                    elif "glassdoor" in sender:
                        category = "Vagas de Emprego"

                    elif "infojobs" in sender:
                        category = "Vagas de Emprego"

                    elif "linkedin" in sender:
                        category = "Networking"

                    elif "hashtag" in sender:
                        category = "Estudos"

                    elif "pinterest" in sender:
                        category = "Promocional"

                    elif "mercado" in sender:
                        category = "Financeiro"

                    elif "panini" in sender:
                        category = "Compras"

                    elif "vaga" in subject:
                        category = "Possível Vaga"

                    # EXIBIÇÃO NO TERMINAL

                    print(f"Categoria: {category}")
                    print(f"Remetente: {msg.from_}")
                    print(f"Assunto: {msg.subject}")
                    print(f"Data: {msg.date}")
                    print("-" * 50)

                    # SALVAR LOGS

                    log_file.write(
                        f"\n[{datetime.now()}]\n"
                    )

                    log_file.write(
                        f"Categoria: {category}\n"
                    )

                    log_file.write(
                        f"Remetente: {msg.from_}\n"
                    )

                    log_file.write(
                        f"Assunto: {msg.subject}\n"
                    )

                    log_file.write(
                        f"Data: {msg.date}\n"
                    )

                    log_file.write(
                        "-" * 50 + "\n"
                    )

    except Exception as error:
        print(f"Erro ao ler emails: {error}")