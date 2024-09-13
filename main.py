from ENTITIES.funcionario import funcionario
from ENTITIES.pedidos import pedido, prioridade, response
from ENTITIES.setor import setor 
from MGR.setorMGR import setorMGR
from MGR.pedidoMGR import pedidoMGR 
from DAO.setorDAO import setorDAO
from DVO.pedidoDVO import pedidoDVO 
from DVO.setorDVO import setorDVO


def main():
    
    ##### Pré requisitos
    setor1 = setor()
    setor2 = setor()
    setor1.setNome("TI")
    setor2.setNome("Manutenção predial")

    setorDAO = setorDAO()
    setorDAO.create()
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

    # Corrigido: chamado o objeto diretamente
    pedidoMGR.realizarPedidoSuporte(pedido, pedido.setor)

    # Corrigido: chamado o objeto diretamente
    pedidoMGR.validarPedido(pedido, "sim")


if __name__ == "__main__":
    main()
