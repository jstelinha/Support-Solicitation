from ENTITIES.funcionario import funcionario
from ENTITIES.pedido import pedido
from ENTITIES.setor import setor    


class pedidoMGR:
    def requisitarSuporte(pedido:object, setor:object):
        try:
            suporte = pedido()
            suporte.setResponse("pendente")
            setor.setPedidos(suporte)

        except Exception as e:
            return e
         
    def validarPedido(pedido:object, response:str):
        try:
            pedido.setResponse(response)
        except Exception as e:
            return e