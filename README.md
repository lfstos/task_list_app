# Task List App

Este é um aplicativo da web baseado em Django que permite aos usuários gerenciar uma lista de proprietários de automóveis e seus carros.

## Features

- Autenticação de usuário usando Django-allauth
- Operações CRUD para proprietários de automóveis e carros
- Rotas seguras com login necessário
- Testes unitários para a funcionalidade principal

## Pré requisitos

- Docker e Docker Compose instalados em seu sistema

## Começando
```
1. git clone https://github.com/lfstos/task_list_app.git

2. cd task_list_app.git

3. python -m venv .venv

4. source .venv/bin/activate

5. pip install -r requirements.txt
```

2. Crie e execute os contêineres Docker:

```
Isso criará e iniciará os seguintes contêineres:
- `web`: A aplicação Django
- `db`: O Banco de Dados PostgreSQL
```

3. Assim que os contêineres estiverem funcionando, você poderá acessar o aplicativo em `http://localhost:8000`.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

```
task_list_app/
├── core/
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── cars/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── account/
│   │   ├── login.html
│   │   └── signup.html
│   └── cars/
│       ├── owner_list.html
│       ├── owner_create.html
│       ├── car_list.html
│       └── car_create.html
├── Dockerfile
├── docker-compose.yml
├── manage.py
└── requirements.txt
```

- `core/`: O diretório principal do projeto Django.
- `cars/`: O aplicativo Django que cuida do proprietário e do gerenciamento do carro.
- `templates/`: Os modelos HTML usados ​​pelo aplicativo.
- `Dockerfile`: O arquivo de configuração do Docker para o aplicativo Django.
- `docker-compose.yml`: O arquivo de configuração do Docker Compose para toda a pilha de aplicativos.
- `manage.py`: O script de gerenciamento do Django.
- `requirements.txt`: As dependências do Python para o projeto.

## Executando os Testes

Isso executará os testes definidos no arquivo `cars/tests.py`.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

