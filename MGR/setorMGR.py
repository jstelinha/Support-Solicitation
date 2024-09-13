from ENTITIES.pedidos import *
from DAO.setorDAO import *


class setorMGR:
        def listarSetor(self):
            try:
                setorDAO = setorDAO.create()
                return setorDAO.listaSetores()
        
            except Exception as e:
                return e