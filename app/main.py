# Importa a classe principal para criar a aplicação Web
from fastapi import FastAPI

# Importa a estrutura do banco (Base) e o motor de conexão (engine)
from app.database import Base, engine
# Importa os módulos de rotas que você desenvolveu (Usuários e Produtos)
from app.routes import products, users

# Este comando verifica seus modelos e cria as tabelas 'users' e 'products' 
# no banco de dados SQLite caso elas ainda não existam.
Base.metadata.create_all(bind=engine)

# Inicializa o FastAPI com as informações que aparecerão no cabeçalho da documentação
app = FastAPI(
    title="Mini Sistema de Pedidos",
    description="API REST para simular um sistema simples de pedidos.",
    version="1.0.0"
)

# Registra as rotas de usuários. Endereços como /users/ funcionarão agora.
app.include_router(users.router)

# Registra as rotas de produtos. Endereços como /products/ funcionarão agora.
# O FastAPI vai separar esses dois grupos na documentação /docs automaticamente.
app.include_router(products.router)

# Rota raiz (ponto de entrada) para verificar se o servidor está ligado.
@app.get("/")
def home():
    """Retorna um JSON simples de boas-vindas."""
    return {
        "mensagem": "API do Mini Sistema de Pedidos funcionando!"
    }