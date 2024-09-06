from ENTITIES.pedido import pedido
from DAO.setorDAO import setorDAO


class setorMGR:
    def entregaRelatorio(response:str, pedido:object):
        try:
            setorDAO.create()
        except Exception as e:
            return e
