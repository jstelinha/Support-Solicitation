from ENTITIES.fPedido import fPedido
from ENTITIES.pedido import pedido
import DAO.setorDAO 


class setorMGR:
    def RegistrarAndamento(status:str, data:int):
        try:
            fluxo = fPedido()
            fluxo.setStatus(status)
            fluxo.setData(data)
            
        except Exception as e:
            return e

    def ValidarPedido(self, response:str, pedido:object):
        try:
            pedido.setResponse(response)
        except Exception as e:
            return e
