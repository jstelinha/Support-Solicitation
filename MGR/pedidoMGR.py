from DAO.PedidoDAO import PedidoDAO
from DAO.SetorDAO import SetorDAO


class PedidoMGR:
    
    def listarPrioridadePedido(self):
        try:
            pedidoDAO = PedidoDAO.create()
            return pedidoDAO.listPrioridades()
        
        except Exception as e:
            return e
    
    def listarResponse(self):
        try:
            pedidoDAO = PedidoDAO.create()
            return pedidoDAO.listResponse()
        
        except Exception as e:
            return e

    
    def realizarPedidoSuporte(pedido:object, setor:object):
        try:
            PedidoDAO.create()
            SetorDAO.create()
            pedido.setResponse(PedidoMGR.listarResponse()[2])
            setor.setPedidos(pedido.idPedido)
            PedidoDAO.update(pedido)
            SetorDAO.update(setor)
            return SetorDAO.listPedidosById(pedido.idPedido)

        except Exception as e:
            return e


