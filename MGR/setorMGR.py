import DAO.setorDAO 
from ENTITIES.fPedido import fPedido
class setor:
    def __init__(self, ids:int, nome):
        self.id = ids
        self.nome = nome

    def RegistrarAndamento(status:str, data:int):
        try:
            fluxo = fPedido()
            fluxo.setData(data)
            fluxo.setStatus(status)
            
        except Exception as e:
            return e

    def RealizarRelatorio(self):


    def ValidarPedido(self):
