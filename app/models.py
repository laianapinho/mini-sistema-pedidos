from sqlalchemy import Boolean, Column, Float, Integer, String
from app.database import Base

# --- MODELO DE USUÁRIO ---
class User(Base):
    """Representa a tabela de clientes/usuários do sistema."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) # Identificador único
    nome = Column(String, nullable=False)              # Nome obrigatório
    email = Column(String, unique=True, index=True, nullable=False) # E-mail único
    telefone = Column(String, nullable=True)           # Telefone opcional


# --- MODELO DE PRODUTO ---
class Product(Base):
    """
    Representa a tabela de produtos disponíveis para venda.
    """
    # Define o nome da tabela no banco de dados como 'products'
    __tablename__ = "products"

    # ID do produto: Chave primária para identificar cada item
    id = Column(Integer, primary_key=True, index=True)

    # Nome do produto: Texto obrigatório (ex: "Pizza de Calabresa")
    nome = Column(String, nullable=False)

    # Descrição: Texto opcional para dar detalhes do produto
    descricao = Column(String, nullable=True)

    # Preço: Float (número decimal) obrigatório para armazenar o valor
    preco = Column(Float, nullable=False)

    # Disponível: Booleano (Verdadeiro/Falso). 
    # Por padrão (default), todo produto novo é criado como disponível (True).
    disponivel = Column(Boolean, default=True)