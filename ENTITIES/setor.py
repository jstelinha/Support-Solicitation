class setor:
    def __init__(self, ids:int, nome):
        self.pedidos = []
        self.nome = nome
        self.id = ids
        
    def setPedidos(self, pedido:object):
        self.pedidos.append(pedido)
