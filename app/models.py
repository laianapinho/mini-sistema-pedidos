# Importa os tipos de dados (Inteiro e Texto) e a classe Column do SQLAlchemy
from sqlalchemy import Column, Integer, String

# Importa a classe Base que configuramos no arquivo database.py
# Ela é necessária para que o SQLAlchemy "enxergue" esta classe como uma tabela
from app.database import Base


class User(Base):
    """
    Representa a tabela de usuários no banco de dados.
    """
    # Define explicitamente o nome da tabela no banco de dados
    __tablename__ = "users"

    # Chave Primária: Identificador único de cada usuário.
    # index=True cria um índice para que buscas por ID sejam instantâneas.
    id = Column(Integer, primary_key=True, index=True)

    # Nome do usuário: Uma coluna de texto que não pode estar vazia (nullable=False).
    nome = Column(String, nullable=False)

    # E-mail:
    # unique=True: Garante que não existam dois usuários com o mesmo e-mail.
    # index=True: Otimiza a performance, já que e-mail é muito usado em logins.
    # nullable=False: Campo obrigatório.
    email = Column(String, unique=True, index=True, nullable=False)

    # Telefone: Uma coluna de texto que é opcional (nullable=True).
    telefone = Column(String, nullable=True)
