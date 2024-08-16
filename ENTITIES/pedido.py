class pedido:
    def __init__(self, ids:int):
        self.prioridades = ["emergencia", "alta", "media", "baixa", "minima"]
        self.id = ids

    def setDescrip(self, desc:str):
        if desc in self.status:
            self.desc = desc
    
    def setPriority(self, priority:str):
        if priority in self.prioridades:
            self.prioridade = priority
    
    def setResponse(self, response:str):
        if response.lower() in ["sim","nao", "y", "n", "s"]:
            self.response = response