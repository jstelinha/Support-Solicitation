from ENTITIES.fluxo import fPedido
from DAO.fluxoDAO import fluxoDAO


class fluxoMGR:
    def RegistrarAndamento(pedido:object ,status:str, data:int):
        try:
            fluxo = fPedido()
            fluxo.setStatus(status)
            fluxo.setData(data)
            fluxoDAO.create()
            return fluxoDAO.listByIds(fluxoDAO.ids)

        except Exception as e:
            return e