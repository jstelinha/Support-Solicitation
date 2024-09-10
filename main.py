from ENTITIES.funcionario import *
from ENTITIES.pedido import * 
from ENTITIES.setor import * 
from MGR.setorMGR import *
from MGR.pedidoMGR import * 
from DAO.pedidoDAO import * 
from DAO.setorDAO import *
from DVO.pedidoDVO import * 
from DVO.setorDVO import *


def main():

    ##### Pré requisitos
    setor1 = setor(1, "TI")
    setor2 = setor(2, "Manutenção predial")

    setorDAO.update(setor1)
    setorDAO.update(setor2)

    gerente = funcionario().gerente()
    assistente = funcionario().assistente()
    requerente = funcionario().requerente()
    gerente.setStatus("ativo")
    gerente.setSetor("TI")
    assistente.setStatus("ativo")
    assistente.setSetor("TI")
    requerente.setStatus("ativo")


    ### Caso de uso Requisitar Suporte
    listaSetores = setorMGR.listarSetor()
    listaPrioridade = pedidoMGR.listarPrioridadePedido()
    listaResponse = pedidoMGR.listarResponse()

    pedido = pedido(requerente.login, listaSetores[0])
    pedido.setDescrip("Um monitor da sala xxxx precisa ser consertado.")
    pedido.setPriority(listaPrioridade[0])

    pedidoMGR.realizarPedidoSuporte(pedido(), pedido.setor)
##################################################################################################

    pedidoMGR.validarPedido(pedido(), "sim")

main()
