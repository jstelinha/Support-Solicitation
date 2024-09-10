from ENTITIES.fluxo import *
from DAO.fluxoDAO import *


class fluxoMGR:
    def RegistrarAndamento(pedido:object, status:str, data:int):
        try:
            fluxo = fPedido()
            fluxo.setStatus(status)
            fluxo.setData(data)
            fluxoDAO.create()
            return fluxoDAO.listByIds(pedido.idPedido)

        except Exception as e:
            return e