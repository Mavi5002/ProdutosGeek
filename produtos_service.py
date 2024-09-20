from sqlmodel import Session, select
from sqlalchemy import update
from database import get_engine
from models import Produto
from fastapi import status, HTTPException
from dtos import ProdutoDTO,EstoqueAtualiza

class ProdutoService():
    def __init__(self):#inicializa uma sessão com o banco de dados
        engine = get_engine
        self.session = Session(engine)
        #interface usado para interaçao com o banco de dados

    #Faz uma busca pelo numero de indentificação
    def get_produto_by_id(self,id: int):
        #sttm:statement(consulta)

        sttm = select(Produto).where(Produto.id==id)
        return self.session.exec(sttm).one_or_none()
        #retorna um unico resultado da consulta se houver um registro correspondente
    
    #funçao de busca por um filtro especifico
    def get_all_produtos(self, nome: str| None = None , preço: float| None = None, categoria:str |None = None, franquia:str |None = None ):
        sttm = select(Produto)

        if nome:
            sttm = sttm.where(Produto.nome.in_(nome))
        
        if nome:
            sttm = sttm.where(Produto.preço.in_(preço))

        if categoria:
            sttm = sttm.where(Produto.categoria.in_(categoria))
        
        if franquia:
            sttm = sttm.where(Produto.franquia.in_(franquia))
        
        return self.session.exec(sttm).all
    

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
        return{"OK":status.HTTP_200_OK}
       

    
    def save_produto(self, produto: Produto):
        self.session.add(produto)
        self.session.commit()
        self.session.refresh(produto)
        return produto


    
        