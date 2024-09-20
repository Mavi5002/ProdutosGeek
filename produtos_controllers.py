from fastapi import APIRouter, status, HTTPException
from models import Produto
from ulid import ULID
from sqlmodel import Session,select
from database import get_engine
from produtos_service import ProdutoService


router = APIRouter()

produtos_service = ProdutoService()


#criar novo produto
@router.post("/",response_model=Produto,
             status_code=status.HTTP_201_CREATED)
def novo_produto(produto:Produto):
    novo = Produto(nome=produto.nome,
                    descriçao =produto.descriçao,
                    preço=produto.preço,
                    categoria= produto.categoria,
                    franquia=produto.franquia)

    return produtos_service.save_produto(novo_produto)





#lista produtos
""" @router.get('/', response_model=list[Produto])
def produtos_list(nome: str | None = None,
                  preço: float| None = None,
                  categoria:str |None = None,
                  franquia:str |None = None 
                  ):
  
    produtos = produtos_service.get_all_produtos(nome,preço,categoria,franquia)
    if not produtos:
        raise HTTPException(status_code=404, detail="Nenhum produto encontrado")

    return produtos
 """












""" @router.put('/{id}/cancel')
def produto_cancel(id: str):
  produto_localizada = produtos_service.get_corrida_by_id(id)

  if not produto_localizada:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail='Produto não localizado!')
  
  if not produto_localizada.id in:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail='Não é possível cancelar esta corrida!')
  
  corrida_localizada.estado = 'cancelada'

  return corrida_service.save_corrida(corrida_localizada) """