class setor:
    def __init__(self, ids:int, nome:str):
        self.pedidos = []
        self.nome = nome
        self.idSetor = ids
        
    def setPedidos(self, idPedido:int):
        self.pedidos.append(idPedido)
