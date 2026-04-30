from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define o endereço do banco de dados. 
# Nesse caso, um arquivo local chamado 'mini_pedidos.db' usando SQLite.
DATABASE_URL = "sqlite:///./mini_pedidos.db"

# Cria o 'engine' (motor), que é o centro de controle que gerencia 
# a conexão real com o arquivo do banco de dados.
engine = create_engine(
    DATABASE_URL, 
    # check_same_thread=False é necessário apenas para o SQLite no FastAPI 
    # para permitir que várias requisições acessem o banco ao mesmo tempo.
    connect_args={"check_same_thread": False}
)

# Cria uma fábrica de sessões (SessionLocal). 
# Cada instância de sessão será uma "transação" com o banco.
SessionLocal = sessionmaker(
    autocommit=False, # Não salva automaticamente; exige o comando db.commit()
    autoflush=False,   # Não envia mudanças para o banco antes de você pedir
    bind=engine       # Conecta esta fábrica ao motor criado acima
)

# Cria a classe Base. Todos os nossos modelos (tabelas) vão herdar 
# desta classe para serem reconhecidos pelo SQLAlchemy.
Base = declarative_base()


# Função de Dependência (Dependency Injection) para o FastAPI.
def get_db():
    """
    Cria uma nova sessão de banco de dados para cada requisição 
    e garante que ela seja fechada após o uso.
    """
    db = SessionLocal() # Abre a conexão/sessão
    try:
        yield db       # Entrega a sessão para quem chamou (o endpoint)
    finally:
        db.close()     # Fecha a conexão obrigatoriamente, mesmo se houver erro
