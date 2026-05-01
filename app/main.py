# Importa a classe FastAPI para criar o servidor web
from fastapi import FastAPI

# Importa a estrutura do banco (Base) e o motor de conexão (engine)
from app.database import Base, engine
# Importa todos os roteadores que você criou: pedidos, produtos e usuários
from app.routes import orders, products, users

# Comando "mágico" do SQLAlchemy: verifica todos os modelos (User, Product, Order)
# e cria as tabelas automaticamente no banco de dados se elas não existirem.
Base.metadata.create_all(bind=engine)

# Instancia o aplicativo FastAPI e define os metadados para a documentação técnica
app = FastAPI(
    title="Mini Sistema de Pedidos",
    description="API REST para simular um sistema simples de pedidos.",
    version="1.0.0"
)

# Registra as rotas de usuários no sistema principal
app.include_router(users.router)

# Registra as rotas de produtos no sistema principal
app.include_router(products.router)

# Registra as rotas de pedidos, fechando o ciclo do sistema
app.include_router(orders.router)

# Define uma rota de "boas-vindas" ou teste de saúde (health check)
@app.get("/")
def home():
    """Retorna um JSON simples confirmando que a API está no ar."""
    return {
        "mensagem": "API do Mini Sistema de Pedidos funcionando!"
    }