from ENTITIES.funcionario import funcionario
from ENTITIES.pedido import pedido
from ENTITIES.setor import setor   
from DAO.pedidoDAO import pedidoDAO
from DAO.setorDAO import setorDAO


class pedidoMGR:
    def listarSetor(self):
        setorDAO = setorDAO.create()
        return setorDAO.list()
    
    def listarPrioridadePedido(self):
        pedidoDAO = pedidoDAO.create()
        return pedidoDAO.listPrioridades()
    
    def listarResponse(self):
        pedidoDAO = pedidoDAO.create()
        return pedidoDAO.listResponse
    
    def realizarPedidoSuporte(pedido:object, setor:object):
        try:
            pedidoDAO.create()
            setorDAO.create()
            pedido.setResponse()
            setor.setPedidos(pedido.idPedido)
            pedidoDAO.update(pedido)
            setorDAO.update(setor)
            return setorDAO.listPedidosById(pedido.idPedido)

        except Exception as e:
            return e


