class pedido:
    def __init__(self):
        self.prioridades = ["emergencia", "alta", "media", "baixa", "minima"]

    def setDescrip(self, desc:str):
        if desc in self.status:
            self.desc = desc
    
    def setPriority(self, priority:str):
        if priority.lower() in self.prioridades:
            self.prioridade = priority
    
    def setResponse(self, response:str):
        if response.lower() in ["sim","nao", "pendente", "y", "n", "s", "p"]:
            self.response = response