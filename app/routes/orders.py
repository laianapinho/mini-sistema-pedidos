from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Importa a conexão, os modelos de banco e os validadores de pedidos
from app.database import get_db
from app.models import Order, Product, User
from app.schemas import OrderCreate, OrderResponse

# Configura o roteador para o caminho /orders
router = APIRouter(
    prefix="/orders",
    tags=["Pedidos"]
)

# --- ROTA PARA CRIAR UM PEDIDO (POST) ---
@router.post("/", response_model=OrderResponse, status_code=201)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """
    Cria um pedido realizando validações de existência e cálculos de preço.
    """
    # 1. Validação de Segurança: O usuário que está comprando existe?
    user = db.query(User).filter(User.id == order.user_id).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )

    # 2. Validação de Segurança: O produto solicitado existe?
    product = db.query(Product).filter(Product.id == order.product_id).first()
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    # 3. Regra de Negócio: O produto pode até existir, mas ele está ativo para venda?
    if not product.disponivel:
        raise HTTPException(
            status_code=400,
            detail="Produto indisponível para pedido."
        )

    # 4. Cálculo Automático: Multiplica o preço atual do produto pela quantidade pedida.
    # Isso evita que o cliente altere o preço manualmente na requisição.
    valor_total = product.preco * order.quantidade

    # 5. Montagem do Objeto: Cria o registro do pedido com o status inicial.
    new_order = Order(
        user_id=order.user_id,
        product_id=order.product_id,
        quantidade=order.quantidade,
        valor_total=valor_total,
        status="CRIADO"
    )

    db.add(new_order)       # Prepara a gravação
    db.commit()            # Salva no banco de dados
    db.refresh(new_order)   # Carrega o ID e a data de criação gerados

    return new_order


# --- ROTA PARA LISTAR TODOS OS PEDIDOS (GET) ---
@router.get("/", response_model=list[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    """Retorna uma lista com todo o histórico de pedidos."""
    orders = db.query(Order).all()
    return orders


# --- ROTA PARA BUSCAR UM PEDIDO ESPECÍFICO (GET por ID) ---
@router.get("/{order_id}", response_model=OrderResponse)
def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    """Busca os detalhes de um pedido pelo seu ID."""
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado."
        )

    return order