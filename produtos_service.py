from sqlmodel import Session, select
from sqlalchemy import update
from database import get_engine
from models import ProdutoModel
from fastapi import status, HTTPException
from dtos import ProdutoDTO,EstoqueAtualiza

class ProdutoService():
    
    def __init__(self):#inicializa uma sessão com o banco de dados
        engine = get_engine()
        self.session = Session(engine)
        #interface usado para interaçao com o banco de dados

    #Faz uma busca pelo numero de indentificação
    def get_produto_by_id(self, id: int):
        #sttm:statement(consulta)

        sttm = select(ProdutoModel).where(ProdutoModel.id==id)
        return self.session.exec(sttm).one_or_none()
        #retorna um unico resultado da consulta se houver um registro correspondente
    
    #funçao de busca por um filtro especifico
    def get_all_produtos(self, nome: str| None = None , preço: float| None = None, categoria:str |None = None, franquia:str |None = None ):
        if nome != None:
            sttm = select(ProdutoModel).where(ProdutoModel.nome==nome)
        
        elif preço != None:
            sttm = select(ProdutoModel).where(ProdutoModel.preço==preço)
        
        elif categoria != None:
            sttm = select(ProdutoModel).where(ProdutoModel.categoria==categoria)
        
        elif franquia != None:
            sttm = select(ProdutoModel).where(ProdutoModel.franquia==franquia)
        
        else:
            sttm = select(ProdutoModel)
        
        return self.session.exec(sttm).all()
    
    def save_produto(self, produto: ProdutoModel):
        self.session.add(produto)
        self.session.commit()
        self.session.refresh(produto)
        return produto

    def atualiza_estoque(self, id:int, dado_estoque:EstoqueAtualiza):
        produto = self.get_produto_by_id(id)
        if not produto:
            raise ValueError("Produto não encontrado em estoque")
        
        nova_quantidade = produto.quantidade_estoque + dado_estoque.quantidade

        if nova_quantidade < 0:
            raise ValueError("Não é possivel a venda")
        
        produto.quantidade_estoque = nova_quantidade
        self.session.commit()
        self.session.refresh(produto)
        return produto
    
    
    def remove_produto(self,id: int):
        produto = self.get_produto_by_id(id)
        #produtos que nao estao em estoque nao é possivel deletar
        if produto.quantidade_estoque > 0:
            raise HTTPException(status_code=400)
        
    
        self.session.delete(produto)
        self.session.comit()
        return{"OK": status.HTTP_200_OK}
       

    
    


    
        