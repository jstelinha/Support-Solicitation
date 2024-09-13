class Pedidos:
    def __init__(self, loginFuncionario:str, nSetor:int):
        self.loginFuncionario = loginFuncionario
        self.idPedido = nSetor

    def setDescrip(self, desc:str):
        if desc in self.status:
            self.desc = desc
    
    def setPriority(self, priority:object):
        self.prioridade = priority
    
    def setResponse(self, response:str):
        if response.lower() in ["sim","nao", "pendente", "y", "n", "s", "p"]:
            self.response = response


class prioridade:
    def __init__(self, nivel, nome):
        self.nivel = nivel
        self.nome = nome
    def lista():
        emergencia = prioridade(1, "Emergência")
        alta = prioridade(2, "Alta")
        media = prioridade(3, "Média")
        baixa = prioridade(4, "Baixa")
        minima  = prioridade(5, "Mínima")
        return [emergencia, alta, media, baixa, minima]

class response:
    def __init__(self, response):
        self.response = response
    def lista():
        sim = response("Sim")
        nao = response("Não")
        pendente = response("Pendente")
        return [sim,nao,pendente]