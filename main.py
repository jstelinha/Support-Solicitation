from ENTITIES.funcionario import funcionario
from ENTITIES.pedido import pedido 
from ENTITIES.setor import setor 
from MGR.setorMGR import setorMGR
from MGR.pedidoMGR import pedidoMGR 
from DAO.pedidoDAO import pedidoDAO 
from DAO.setorDAO import setorDAO
from DVO.pedidoDVO import pedidoDVO 
from DVO.setorDVO import setorDVO


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
    listaSetores = setorMGR.listaSetores()
    listaPrioridade = pedidoMGR.listarPrioridadePedido()
    listaResponse = pedidoMGR.

    pedido = pedido(requerente.login, listaSetores[0])
    pedido.setDescrip("Um monitor da sala xxxx precisa ser consertado.")
    pedido.setPriority(listaPrioridade[0])

    pedidoMGR.realizarPedidoSuporte(pedido(), setor1())
##################################################################################################

    pedidoMGR.validarPedido(pedido(), "sim")

main()
