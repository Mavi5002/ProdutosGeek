from fastapi import APIRouter, status, HTTPException
from models import ProdutoModel
from database import get_engine
from produtos_service import ProdutoService
from dtos import ProdutoDTO,EstoqueAtualiza
""" from sqlmodel import Session,select """

router = APIRouter()

produtos_service = ProdutoService()


@router.get("/{id}")
def get_produto_by_id(id:int):
    return produtos_service.get_produto_by_id(id=id)


@router.get("/")
def produtos_lista(nome: str| None = None , preço: float| None = None, categoria:str |None = None, franquia:str |None = None):
    return produtos_service.get_all_produtos(nome=nome,preço=preço,categoria=categoria,franquia=franquia)




#criar novo produto
@router.post("/",
             response_model=ProdutoModel,
             status_code=status.HTTP_201_CREATED)
def novo_produto(produto:ProdutoDTO):
    novo = ProdutoModel(
                    nome=produto.nome,
                    descriçao=produto.descriçao,
                    preço=produto.preço,
                    categoria= produto.categoria,
                    franquia=produto.franquia,
                    quantidade_estoque=produto.quantidade_estoque)

    return produtos_service.save_produto(novo)





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