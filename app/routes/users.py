from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Importa as ferramentas de conexão, os modelos do banco e os validadores (schemas)
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse

# Cria o roteador para organizar as rotas de usuários
router = APIRouter(
    prefix="/users",    # Todos os endereços começarão com /users
    tags=["Usuários"]   # Agrupa estas rotas na documentação automática
)

# --- ROTA PARA CRIAR UM USUÁRIO (POST) ---
@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Cadastra um novo usuário, verificando primeiro se o e-mail já existe.
    """
    # Consulta o banco de dados para ver se o e-mail enviado já está cadastrado
    email_exists = db.query(User).filter(User.email == user.email).first()

    # Se encontrar algo, interrompe a execução e retorna erro 400 (Bad Request)
    if email_exists:
        raise HTTPException(
            status_code=400,
            detail="Já existe um usuário cadastrado com este e-mail."
        )

    # Transforma os dados que vieram da requisição (schema) em um modelo de banco (SQLAlchemy)
    new_user = User(
        nome=user.nome,
        email=user.email,
        telefone=user.telefone
    )

    db.add(new_user)       # Prepara a inserção no banco
    db.commit()            # Confirma a transação e salva os dados
    db.refresh(new_user)   # Atualiza o objeto 'new_user' com o ID gerado pelo banco

    return new_user


# --- ROTA PARA LISTAR TODOS OS USUÁRIOS (GET) ---
@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    """Busca e retorna uma lista com todos os usuários do banco."""
    users = db.query(User).all() # SELECT * FROM users
    return users


# --- ROTA PARA BUSCAR UM USUÁRIO ESPECÍFICO (GET por ID) ---
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """Busca um usuário pelo ID; retorna 404 se não for encontrado."""
    # Filtra no banco pelo ID passado na URL
    user = db.query(User).filter(User.id == user_id).first()

    # Valida se o usuário existe
    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )

    return user
