from datetime import datetime

# Importa os tipos de colunas e ferramentas de relacionamento do SQLAlchemy
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

# --- TABELA DE USUÁRIOS ---
class User(Base):
    __tablename__ = "users" # Nome da tabela no banco

    id = Column(Integer, primary_key=True, index=True) # Chave primária única
    nome = Column(String, nullable=False)              # Texto obrigatório
    email = Column(String, unique=True, index=True, nullable=False) # E-mail único e indexado
    telefone = Column(String, nullable=True)           # Campo opcional

    # Cria uma relação virtual para acessar os pedidos do usuário via código: usuario.orders
    orders = relationship("Order", back_populates="user")


# --- TABELA DE PRODUTOS ---
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    preco = Column(Float, nullable=False)              # Preço com casas decimais
    disponivel = Column(Boolean, default=True)         # Status ativo/inativo

    # Cria uma relação virtual para ver quais pedidos contêm este produto
    orders = relationship("Order", back_populates="product")


# --- TABELA DE PEDIDOS (A TABELA DE LIGAÇÃO) ---
class Order(Base):
    """
    Esta classe une Usuários e Produtos. 
    Ela registra QUEM comprou, O QUE comprou e QUANTOS comprou.
    """
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    
    # ForeignKey: Vincula este pedido a um ID existente na tabela 'users'
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # ForeignKey: Vincula este pedido a um ID existente na tabela 'products'
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    
    quantidade = Column(Integer, nullable=False)
    valor_total = Column(Float, nullable=False)        # Resultado do cálculo preco * qtd
    status = Column(String, default="CRIADO")          # Estado do pedido (CRIADO, PAGO, etc)
    
    # Registra o momento exato da compra usando o horário universal (UTC)
    data_criacao = Column(DateTime, default=datetime.utcnow)

    # Define o relacionamento inverso: permite acessar os dados do usuário dentro do pedido
    # Exemplo: pedido.user.nome
    user = relationship("User", back_populates="orders")
    
    # Permite acessar os dados do produto dentro do pedido
    # Exemplo: pedido.product.nome
    product = relationship("Product", back_populates="orders")