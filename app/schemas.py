# BaseModel é a classe base para criar modelos de dados no Pydantic.
# EmailStr é um tipo especial que valida automaticamente se o texto é um e-mail válido.
from pydantic import BaseModel, EmailStr, Field

# Schema para CRIAÇÃO: Define quais dados o cliente deve enviar para cadastrar um usuário.
class UserCreate(BaseModel):
    nome: str                  # Obrigatório: deve ser uma string.
    email: EmailStr            # Obrigatório: deve ser um e-mail válido (ex: user@example.com).
    # O uso de 'str | None = None' (Python 3.10+) indica que o campo é opcional.
    # Se não for enviado, o valor padrão será None.
    telefone: str | None = None


# Schema para RESPOSTA: Define como os dados serão exibidos para o cliente.
class UserResponse(BaseModel):
    id: int                    # Inclui o ID (que não existia no UserCreate).
    nome: str
    email: EmailStr
    telefone: str | None = None

    # Classe de configuração interna do Pydantic.
    class Config:
        # Permite que o Pydantic converta objetos de modelos do banco de dados 
        # (como a classe 'User' do SQLAlchemy) diretamente para este Schema.
        # Sem isso, o Pydantic só aceitaria dicionários.
        from_attributes = True

# --- SCHEMAS DE PRODUTO ---

# Schema para CRIAR um produto
class ProductCreate(BaseModel):
    # min_length=2: Garante que o nome tenha pelo menos 2 caracteres
    nome: str = Field(..., min_length=2) 
    
    descricao: str | None = None
    
    # gt=0: Significa "Greater Than" (Maior que). Impede preços negativos ou zero.
    preco: float = Field(..., gt=0)
    
    # Define que, se não for enviado, o produto nasce como disponível
    disponivel: bool = True


# Schema para ATUALIZAR um produto (Tudo é opcional)
class ProductUpdate(BaseModel):
    # Aqui todos os campos podem ser None, pois você pode querer atualizar só o preço, 
    # ou só o nome, sem precisar reenviar todos os dados do produto.
    nome: str | None = Field(default=None, min_length=2)
    descricao: str | None = None
    preco: float | None = Field(default=None, gt=0)
    disponivel: bool | None = None


# Schema para a RESPOSTA da API ao cliente
class ProductResponse(BaseModel):
    id: int        # O cliente precisa ver o ID gerado pelo banco
    nome: str
    descricao: str | None = None
    preco: float
    disponivel: bool

    class Config:
        # Permite converter o objeto do banco (SQLAlchemy) diretamente para este schema
        from_attributes = True
