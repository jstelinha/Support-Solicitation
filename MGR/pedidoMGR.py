from ENTITIES.funcionario import funcionario
from ENTITIES.pedido import pedido
from ENTITIES.setor import setor    


class pedidoMGR:
    def requisitarSuporte(desc:str, setor:object, priority:str):
        try:
            suporte = pedido()
            suporte.setDescrip(desc)
            suporte.setPriority(priority)
            suporte.setResponse("pendente")
            setor.setPedidos(suporte)

        except Exception as e:
            return e
         
    def validarPedido(suporte:object, response:str):
        try:
            suporte.setResponse(response)
        except Exception as e:
            return e