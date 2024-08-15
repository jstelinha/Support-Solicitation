class funcionario:
    def __init__(self, login:str):
        self.cargos = ["funcionario", "requerente", "gerente"]
        self.status = ["ativo","ferias","inativo"]
        self.login = login

    def setCargo(self, cargo:str):
        if cargo in self.cargos:
            self.cargo = cargo

    def setStatus(self, stats:str):
        if stats in self.status:
            self.stats = stats

    class requerente:
        def __init__(self):
            self.login = funcionario.login
            
    class gerente:
        def __init__(self):
            self.login = funcionario.login

    class assistente:
        def __init__(self):
            self.login = funcionario.login