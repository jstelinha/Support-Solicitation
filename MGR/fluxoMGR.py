from ENTITIES.Fluxo import *
from DAO.FluxoDAO import *


class FluxoMGR:
    def RegistrarAndamento(pedido:object, status:str, data:int):
        try:
            fluxo = FPedido()
            fluxo.setStatus(status)
            fluxo.setData(data)
            FluxoMGR.create()
            return FluxoMGR.listByIds(pedido.idPedido)

        except Exception as e:
            return e