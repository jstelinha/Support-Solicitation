class funcionario:
    def __init__(self, login:str):
        self.status = ["ativo","ferias","inativo"]
        self.login = login

    class requerente:
        def __init__(self):
            self.login = funcionario.login
        
        def setStatus(self, stats:str):
            if stats in self.status:
                self.stats = stats
            
    class gerente:
        def __init__(self):
            self.login = funcionario.login
        
        def setStatus(self, stats:str):
            if stats in self.status:
                self.stats = stats

    class assistente:
        def __init__(self):
            self.login = funcionario.login

        def setStatus(self, stats:str):
            if stats in self.status:
                self.stats = stats