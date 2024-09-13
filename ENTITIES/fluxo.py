class FPedido:
    def __init__(self, idPedido:int):
        self.status = ["retido", "aberto", "cancelado", "concluido", "andamento"]
        self.idPedido = idPedido

    def setStatus(self, stats:str):
        if stats in self.status:
            self.desc = stats
            
    def setData(self, date):
        if date == ("%s/%s/%s"):
            self.data = date