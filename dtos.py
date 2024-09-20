from pydantic import BaseModel

class ProdutoDTO(BaseModel):
    nome:str
    descriçao:str
    preço:float
    quantidade_estoque:int
    categoria:str
    franquia:str


class EstoqueAtualiza(BaseModel):
    quantidade:int