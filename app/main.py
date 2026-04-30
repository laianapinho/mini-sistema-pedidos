# Importa a classe FastAPI do pacote fastapi.
# Essa classe fornece todas as funcionalidades para criar sua aplicação Web.
from fastapi import FastAPI

# Cria uma instância da classe FastAPI.
# Este objeto 'app' é o coração da sua aplicação, onde as rotas serão registradas.
app = FastAPI(
    title="Mini Sistema de Pedidos",                # Nome que aparece na documentação (Swagger).
    description="API REST para simular um sistema simples de pedidos.", # Descrição detalhada da API.
    version="1.0.0"                                # Versão atual do seu software.
)

# O decorador @app.get("/") define uma 'rota'.
# Ele diz ao servidor: "Quando alguém acessar o endereço raiz ('/') via método GET,
# execute a função que vem logo abaixo".
@app.get("/")
def home():
    """
    Função de boas-vindas.
    O FastAPI converte automaticamente o dicionário Python abaixo 
    em um formato JSON, que é o padrão de resposta para APIs.
    """
    return {
        "mensagem": "API do Mini Sistema de Pedidos funcionando!"
    }