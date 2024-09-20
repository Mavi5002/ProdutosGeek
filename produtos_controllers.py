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


@router.put("/{id}")
def atualizar_produto(id:int, dds:ProdutoDTO):
    produto = produtos_service.get_produto_by_id(id=id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Produto não encontrado")
    try:
        produto_atualizado = produtos_service.atualiza_produto(id=id, data=dds)
        return produto_atualizado
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/estoque/{id}")
def atualizar_estoque(id:int, dds:EstoqueAtualiza):
    produto = produtos_service.get_produto_by_id(id=id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Produto não encontrado")
    
    try:
        produto_atualizado = produtos_service.atualiza_estoque(id=id, dados_estoque=dds)
        return produto_atualizado
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{id}")
def delete_produto(id:int):
    return produtos_service.remove_produto(id=id)












