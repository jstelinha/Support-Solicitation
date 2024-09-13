from ENTITIES.Pedidos import *
from DAO.SetorDAO import *


class SetorMGR:
        def listarSetor(self):
            try:
                setorDAO = setorDAO.create()
                return setorDAO.listaSetores()
        
            except Exception as e:
                return e