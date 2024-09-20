from pydantic import BaseModel

class ProdutoDTO(BaseModel):
    nome:str
    desc:str
    preço:float
    qtd_estoque:str
    franquia:str


class EstoqueAtualiza(BaseModel):
    quantidade:int