from sqlmodel import Session, select
from database import get_engine
from models import Produto

class ProdutoService():
    def __init__(self):#inicializa uma sessão com o banco de dados
        engine = get_engine
        self.session = Session(engine)
        #interface usado para interaçao com o banco de dados

    #Faz uma busca pelo numero de indentificação
    def get_corrida_by_id(self,id: int):
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
    
    
    def remove_produto(self,id: int):
        
       produto = self.session.exec(select(Produto).where(Produto.id == id)).one_or_none()

       if produto:
           self.session.delete(produto)
           self.session.comit()
           return True
       else:
           return False


    
    def save_produto(self, produto: Produto):
        self.session.add(produto)
        self.session.commit()
        self.session.refresh(produto)
        return produto


    
        