# 📦 FastAPI + Celery + RabbitMQ + Redis + Docker


## Sistema assíncrono com filas de prioridade, workers dedicados e testes automatizados.

# 🚀 Visão Geral
Este projeto implementa uma API FastAPI com processamento assíncrono usando Celery, RabbitMQ como broker e Redis como backend.
A arquitetura suporta múltiplas filas de prioridade:

critical

high

low

Cada fila possui seu próprio worker dedicado, garantindo isolamento e previsibilidade no processamento.

O projeto inclui:

API FastAPI com endpoint de criação de usuário

Serviço que dispara tasks Celery

Task de envio de email de confirmação

Workers separados por fila

Celery Beat

Flower para monitoramento

Testes automatizados com pytest

Debug com pytest --trace e breakpoint()


🧱 Arquitetura 

    app/
        main.py                # Inicialização do FastAPI \n

        celery_app.py          # Configuração do Celery

        rabbitmq.py            # inicializacoa com pyka nao continuado

    /queues
    │
    ├── routers/
    │   └── user.py            # Endpoint /new_user
    │
    ├── services/
    │   └── user_service.py    # Lógica de criação de usuário + chamada Celery
    │
    ├── tasks/
    │   └── email_tasks.py     # Task send_confirmation_email
    │
    └── tests/
        ├── test_services.py   # Teste do serviço
        ├── test_endpoints.py  # Teste do endpoint
        └── test_tasks.py      # Teste da task

# 🐳 Docker Compose
O projeto usa vários serviços:

    api → FastAPI

    worker_critical → fila critical

    worker_high → fila high

    worker_low → fila low

    beat → Celery Beat

    flower → painel de monitoramento

    redis → backend

    rabbitmq → broker + painel de admin

Subir tudo:


    docker compose up --build

# Painéis:

    Flower → http://localhost:5555

    RabbitMQ → http://localhost:15672 (guest/guest)

# 🔥 Fluxo da Task
    Cliente chama /new_user

    FastAPI recebe o payload

    Serviço create_user() é executado

    Serviço dispara:

    python
    send_confirmation_email.apply_async(
        args=[email],
        queue="high"
    )
    Worker da fila high processa a task

    Task retorna:
    {"status": "sent", "email": email}

# 🧪 Testes Automatizados
    1. Rodar testes:         
        pytest -q
    2. Rodar com debug:

    pytest -q --trace

     Testes incluídos:
        Teste	O que valida
        test_create_user_calls_celery	Serviço chama Celery corretamente
        test_new_user_endpoint	Endpoint funciona e dispara task
        test_send_confirmation_email	Task funciona isoladamente
        test_task_queue	Task está configurada para fila correta

# 🐞 Debug com breakpoint()
    Você pode inspecionar mocks e variáveis internas usando:

    python
    breakpoint()
    pytest --trace

## Comandos úteis no PDB:

    n	executa próxima linha
    s	entra na função
    c	continua execução
    locals()	mostra variáveis locais
    mock.call_args	argumentos enviados
    mock.called	se foi chamado
    mock.call_count	número de chamadas