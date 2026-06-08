# 📧 Sistema de Automação de E-mails

Projeto backend de automação de e-mails desenvolvido com Python, focado em produtividade, organização automática da caixa de entrada e manipulação de mensagens via SMTP e IMAP.

---

# 🚀 Funcionalidades

✅ Envio automático de e-mails via SMTP
✅ Leitura automática da caixa de entrada via IMAP
✅ Filtros inteligentes de categorização
✅ Registro automático de logs
✅ Download automático de anexos
✅ Estrutura modular organizada
✅ Configuração segura com variáveis de ambiente

---

# 🧠 Categorias Inteligentes

O sistema identifica automaticamente o contexto dos e-mails recebidos.

Exemplos:

- LinkedIn → Networking
- Glassdoor / InfoJobs → Vagas de Emprego
- Mercado Pago → Financeiro
- Pinterest → Promocional
- Hashtag Treinamentos → Estudos

---

# 🛠️ Tecnologias Utilizadas

- Python
- smtplib
- imap-tools
- python-dotenv
- Git & GitHub

---

# 📂 Estrutura do Projeto

```bash
email-automation-system/
│
├── attachments/
├── logs/
├── services/
│   ├── email_sender.py
│   └── email_reader.py
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

# ▶️ Como Executar o Projeto

## 1. Clonar repositório

```bash
git clone https://github.com/williamcipriano-dev/email-automation-system.git
```

---

## 2. Criar ambiente virtual

```bash
py -m venv venv
```

---

## 3. Ativar ambiente virtual

```bash
.\venv\Scripts\Activate
```

---

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 5. Configurar variáveis de ambiente

Criar arquivo `.env`

```env
EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app
```

---

## 6. Executar sistema

```bash
py main.py
```

---

# 📌 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

- prática de automação backend
- manipulação de e-mails com Python
- organização de código modular
- utilização prática de Git e GitHub
- construção de portfólio profissional

---

# 👨‍💻 Autor

William Cipriano
