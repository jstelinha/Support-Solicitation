class funcionario:
    def __init__(self):
        self.status = ["ativo","ferias","inativo"]

    class requerente:
        def __init__(self):
            self.login = funcionario.login
        
        def setStatus(self, stats:str):
            if stats in self.status:
                self.stats = stats
            
    class gerente:
        def __init__(self):
            self.login = funcionario.login
        
        def setSetor(self, setor:str):
            self.Setor = setor

        def setStatus(self, stats:str):
            if stats in self.status:
                self.stats = stats

    class assistente:
        def __init__(self):
            self.login = funcionario.login

        def setStatus(self, stats:str):
            if stats in self.status:
                self.stats = stats
            
        def setSetor(self, setor:str):
            self.Setor = setor