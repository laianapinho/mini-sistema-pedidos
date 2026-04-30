from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Importa as ferramentas de banco e os Schemas de Produtos que você criou
from app.database import get_db
from app.models import Product
from app.schemas import ProductCreate, ProductResponse, ProductUpdate

# Define o roteador para organizar as rotas de produtos
router = APIRouter(
    prefix="/products",    # Todas as rotas começarão com /products
    tags=["Produtos"]      # Agrupamento na documentação
)

# --- ROTA PARA CRIAR UM PRODUTO (POST) ---
@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """Cria um novo produto no banco de dados."""
    new_product = Product(
        nome=product.nome,
        descricao=product.descricao,
        preco=product.preco,
        disponivel=product.disponivel
    )
    db.add(new_product)       # Adiciona para inserção
    db.commit()            # Salva no banco
    db.refresh(new_product)   # Atualiza o objeto com o ID gerado
    return new_product

# --- ROTA PARA LISTAR TODOS OS PRODUTOS (GET) ---
@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    """Retorna todos os produtos cadastrados."""
    products = db.query(Product).all()
    return products

# --- ROTA PARA BUSCAR UM PRODUTO POR ID (GET) ---
@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    """Busca um produto específico; erro 404 se não existir."""
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return product

# --- ROTA PARA ATUALIZAR PARCIALMENTE UM PRODUTO (PATCH) ---
@router.patch("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product_data: ProductUpdate, # Dados que o usuário quer mudar
    db: Session = Depends(get_db)
):
    """Atualiza apenas os campos enviados no corpo da requisição."""
    # 1. Busca o produto original no banco
    product = db.query(Product).filter(Product.id == product_id).first()

    # 2. Se não existir, interrompe com erro 404
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    # 3. Converte o Schema Pydantic em um dicionário Python.
    # exclude_unset=True ignora os campos que o usuário NÃO enviou.
    update_data = product_data.model_dump(exclude_unset=True)

    # 4. Percorre o dicionário e aplica as mudanças no objeto do banco
    for field, value in update_data.items():
        setattr(product, field, value) # Ex: product.preco = 25.90

    db.commit()            # Salva as alterações
    db.refresh(product)    # Atualiza o objeto com os novos valores
    return product
