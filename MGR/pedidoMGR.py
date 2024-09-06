from ENTITIES.funcionario import funcionario
from ENTITIES.pedido import pedido
from ENTITIES.setor import setor   
from DAO.pedidoDAO import pedidoDAO 


class pedidoMGR:
    def requisitarSuporte(pedido:object, setor:object):
        try:
            suporte = pedido()
            pedidoDAO.create()
            suporte.setResponse("pendente")
            setor.setPedidos(suporte)
            pedidoDAO.update(suporte)
            return pedidoDAO.listByIds(suporte.ids)

        except Exception as e:
            return e
         
    def validarPedido(pedido:object, response:str):
        try:
            pedido.setResponse(response)
            pedidoDAO.update(pedido)
            return pedidoDAO.listByIds(pedido.ids)
        except Exception as e:
            return e