from sqlmodel import SQLModel, Field
#field atribui caraacteristicas adicionais dos atributos

class ProdutoModel(SQLModel, table=True):
    id:int | None=Field(default=None, primary_key=True)
    nome: str
    descriçao:str
    preço: float
    categoria:str
    franquia:str| None
    quantidade_estoque:int 

""" 
    def adiciona_estoque(self):
        if not self.quantidade_estoque < 0:
            self.quantidade_estoque += 1
    
    def tira_estoque(self):
        if not self.quantidade_estoque < 0:
            self.quantidade_estoque -= 1
            raise Exception() """
