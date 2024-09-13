class Funcionario:
    def __init__(self):
        self.status = ["ativo","ferias","inativo"]

    class Requerente:
        def __init__(self, login:str):
            self.login = Funcionario.login
        
        def setStatus(self, stats:str):
            if stats in self.status:
                self.stats = stats
            
    class Gerente:
        def __init__(self, login:str):
            self.login = Funcionario.login
        
        def setSetor(self, setor:str):
            self.Setor = setor

        def setStatus(self, stats:str):
            if stats in self.status:
                self.stats = stats

    class Assistente:
        def __init__(self, login:str):
            self.login = Funcionario.login

        def setStatus(self, stats:str):
            if stats in self.status:
                self.stats = stats
            
        def setSetor(self, setor:str):
            self.Setor = setor