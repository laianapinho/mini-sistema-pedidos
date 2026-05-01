# Mini Sistema de Pedidos — API REST

API REST desenvolvida com Python e FastAPI para simular o fluxo básico de um sistema de pedidos.

## Objetivo

O objetivo do projeto é praticar desenvolvimento backend, criação de APIs REST, organização de rotas, banco de dados relacional, validação de dados e documentação automática com Swagger.

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite
- Git/GitHub

## Funcionalidades implementadas

- Rota inicial da API
- Cadastro de usuários
- Listagem de usuários
- Busca de usuário por ID
- Cadastro de produtos
- Listagem de produtos
- Busca de produto por ID
- Atualização de produto
- Criação de pedidos
- Listagem de pedidos
- Busca de pedido por ID
- Cálculo automático do valor total do pedido
- Validação de usuário existente
- Validação de produto existente
- Validação de produto disponível
- Validação de quantidade maior que zero
- Validações básicas de dados com Pydantic
- Documentação automática com Swagger

## Funcionalidades planejadas

- Atualização do status do pedido
- Testes automatizados com Pytest
- Dockerização da aplicação
- Autenticação com JWT

## Estrutura do projeto

```txt
mini-sistema-pedidos/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       ├── users.py
│       ├── products.py
│       └── orders.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Como executar o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd mini-sistema-pedidos
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no Linux:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
uvicorn app.main:app --reload
```

Acesse a API no navegador:

```txt
http://127.0.0.1:8000
```

Acesse a documentação Swagger:

```txt
http://127.0.0.1:8000/docs
```

## Endpoints

### Rota inicial

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Verifica se a API está funcionando |

### Usuários

| Método | Rota | Descrição |
|---|---|---|
| POST | `/users/` | Cadastra um usuário |
| GET | `/users/` | Lista todos os usuários |
| GET | `/users/{user_id}` | Busca um usuário por ID |

### Produtos

| Método | Rota | Descrição |
|---|---|---|
| POST | `/products/` | Cadastra um produto |
| GET | `/products/` | Lista todos os produtos |
| GET | `/products/{product_id}` | Busca um produto por ID |
| PATCH | `/products/{product_id}` | Atualiza dados de um produto |

### Pedidos

| Método | Rota | Descrição |
|---|---|---|
| POST | `/orders/` | Cria um pedido |
| GET | `/orders/` | Lista todos os pedidos |
| GET | `/orders/{order_id}` | Busca um pedido por ID |

## Exemplos de requisições

### Criar usuário

```json
{
  "nome": "Laiana Cavalcante",
  "email": "laiana@email.com",
  "telefone": "92999999999"
}
```

### Criar produto

```json
{
  "nome": "Hambúrguer",
  "descricao": "Hambúrguer artesanal com queijo",
  "preco": 25.9,
  "disponivel": true
}
```

### Atualizar produto

```json
{
  "disponivel": false
}
```

Também é possível atualizar apenas o preço:

```json
{
  "preco": 29.9
}
```

### Criar pedido

```json
{
  "user_id": 1,
  "product_id": 1,
  "quantidade": 2
}
```

Resposta esperada:

```json
{
  "id": 1,
  "user_id": 1,
  "product_id": 1,
  "quantidade": 2,
  "valor_total": 51.8,
  "status": "CRIADO",
  "data_criacao": "2026-04-30T00:00:00"
}
```

## Regras de negócio

- Não é permitido cadastrar usuário com e-mail repetido.
- Não é permitido criar pedido para usuário inexistente.
- Não é permitido criar pedido com produto inexistente.
- Não é permitido criar pedido com produto indisponível.
- Não é permitido criar pedido com quantidade menor ou igual a zero.
- O valor total do pedido é calculado automaticamente com base no preço do produto e na quantidade.
- Todo pedido é criado inicialmente com o status `CRIADO`.

## Exemplos de erros tratados

### Usuário não encontrado

```json
{
  "detail": "Usuário não encontrado."
}
```

### Produto não encontrado

```json
{
  "detail": "Produto não encontrado."
}
```

### Produto indisponível

```json
{
  "detail": "Produto indisponível para pedido."
}
```

### E-mail já cadastrado

```json
{
  "detail": "Já existe um usuário cadastrado com este e-mail."
}
```

## Observações

Durante o desenvolvimento, o projeto utiliza SQLite para facilitar a criação e os testes locais. Em uma evolução futura, o banco pode ser migrado para PostgreSQL.

## Próximos passos

- Criar rota para atualizar o status do pedido
- Adicionar testes automatizados com Pytest
- Criar Dockerfile e docker-compose.yml
- Implementar autenticação com JWT
- Melhorar a organização do projeto em camadas
```
