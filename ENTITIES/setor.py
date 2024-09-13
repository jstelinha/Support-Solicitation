class setor:
    def __init__(self, nome:str):
        self.pedidos = []
        self.nome = nome
        
    def setPedidos(self, idPedido:int):
        self.pedidos.append(idPedido)
