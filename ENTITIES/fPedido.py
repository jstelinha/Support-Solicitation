class fPedido:
    def __init__(self, pedido:object):
        self.status = ["retido", "aberto", "cancelado", "concluido", "andamento"]
        self.pedido = pedido

    def setStatus(self, stats:str):
        if stats in self.status:
            self.desc = stats
    
    def setData(self, date):
        if date == ("%s/%s/%s"):
            self.data = date
    