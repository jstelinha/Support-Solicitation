from DAO.pedidoDAO import pedidoDAO
from DAO.setorDAO import setorDAO


class pedidoMGR:
    
    def listarPrioridadePedido(self):
        try:
            pedidoDAO = pedidoDAO.create()
            return pedidoDAO.listPrioridades()
        
        except Exception as e:
            return e
    
    def listarResponse(self):
        try:
            pedidoDAO = pedidoDAO.create()
            return pedidoDAO.listResponse()
        
        except Exception as e:
            return e

    
    def realizarPedidoSuporte(pedido:object, setor:object):
        try:
            pedidoDAO.create()
            setorDAO.create()
            pedido.setResponse(pedidoMGR.listarResponse()[2])
            setor.setPedidos(pedido.idPedido)
            pedidoDAO.update(pedido)
            setorDAO.update(setor)
            return setorDAO.listPedidosById(pedido.idPedido)

        except Exception as e:
            return e


