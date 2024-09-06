from ENTITIES.pedido import pedido
from DAO.setorDAO import setorDAO


class setorMGR:
    def entregaRelatorio(response:str, setor:object):
        try:
            setorDAO.create()
            setorDAO.update(setor)
            return setorDAO.listRelatorio(setor.nome) 
        except Exception as e:
            return e
