from sqlalchemy import table
from sqlmodel import SQLModel, Field
#field atribui caraacteristicas adicionais dos atributos

class Produto(SQLModel, table=True):
    id:int = Field(default=None, primary_key=True)
    nome: str
    descriçao:str
    preço: float
    categoria:str
    franquia:str
    quantidade_estoque:int = 0


    def adiciona_estoque(self):
        if not self.quantidade_estoque < 0:
            self.quantidade_estoque += 1
    
    def tira_estoque(self):
        if not self.quantidade_estoque < 0:
            self.quantidade_estoque -= 1
            raise Exception()
