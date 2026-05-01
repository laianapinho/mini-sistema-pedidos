# Mini Sistema de Pedidos — API REST

API REST desenvolvida com **Python** e **FastAPI** para simular o fluxo básico de um sistema de pedidos.

O projeto permite cadastrar usuários, cadastrar produtos, listar registros e atualizar informações de produtos. Nas próximas etapas, serão adicionadas as funcionalidades de criação de pedidos, atualização de status, testes automatizados e dockerização.

---

## Objetivo

O objetivo deste projeto é praticar conceitos de **Engenharia de Software** e **desenvolvimento backend**, incluindo:

- Criação de APIs REST;
- Organização de rotas;
- Modelagem de banco de dados relacional;
- Validação de dados;
- Integração com banco SQLite;
- Documentação automática com Swagger;
- Boas práticas de estruturação de projeto.

---

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite
- Git/GitHub

---

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
├── requirements.txt
└── README.md
```

---

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
- Validações básicas de dados com Pydantic
- Documentação automática com Swagger

---

## Funcionalidades planejadas

- Criação de pedidos;
- Listagem de pedidos;
- Busca de pedido por ID;
- Cálculo automático do valor total do pedido;
- Atualização do status do pedido;
- Testes automatizados com Pytest;
- Autenticação com JWT;
- Dockerização da aplicação.

---

## Como executar o projeto no Linux

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd mini-sistema-pedidos
```

### 2. Criar o ambiente virtual

```bash
python3 -m venv venv
```

### 3. Ativar o ambiente virtual

```bash
source venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
uvicorn app.main:app --reload
```

### 6. Acessar a API

Abra no navegador:

```txt
http://127.0.0.1:8000
```

### 7. Acessar a documentação Swagger

Abra no navegador:

```txt
http://127.0.0.1:8000/docs
```

---

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
| GET | `/users/{user_id}` | Busca um usuário pelo ID |

### Produtos

| Método | Rota | Descrição |
|---|---|---|
| POST | `/products/` | Cadastra um produto |
| GET | `/products/` | Lista todos os produtos |
| GET | `/products/{product_id}` | Busca um produto pelo ID |
| PATCH | `/products/{product_id}` | Atualiza parcialmente um produto |

### Pedidos

| Método | Rota | Descrição |
|---|---|---|
| POST | `/orders/` | Cria um pedido |
| GET | `/orders/` | Lista pedidos |
| GET | `/orders/{order_id}` | Busca pedido por ID |

---

## Exemplos de requisição

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

Para atualizar somente a disponibilidade:

```json
{
  "disponivel": false
}
```

Para atualizar somente o preço:

```json
{
  "preco": 29.9
}
```

---

## Banco de dados

O projeto utiliza SQLite para facilitar o desenvolvimento inicial.

O arquivo do banco será criado automaticamente na raiz do projeto com o nome:

```txt
mini_pedidos.db
```

---

## Status do projeto

Projeto em desenvolvimento.

Etapas concluídas:

- Configuração inicial da API;
- Integração com banco SQLite;
- Cadastro e consulta de usuários;
- Cadastro, consulta e atualização de produtos.

Próxima etapa:

- Implementação da criação e listagem de pedidos.

---

## Autora

**Laiana de Pinho Cavalcante**

- GitHub: laianapinho
- LinkedIn: laiana-cavalcante
