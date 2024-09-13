from ENTITIES.Funcionario import Funcionario
from ENTITIES.Pedidos import Pedidos, prioridade, response
from ENTITIES.Setor import Setor 
from MGR.SetorMGR import SetorMGR
from MGR.PedidoMGR import PedidoMGR 
from DAO.SetorDAO import SetorDAO
from DVO.PedidoDVO import PedidoDVO 
from DVO.SetorDVO import SetorDVO


def main():
    
    ##### Pré requisitos
    setor1 = Setor()
    setor2 = Setor()
    setor1.setNome("TI")
    setor2.setNome("Manutenção predial")

    setorDAO = SetorDAO()
    setorDAO.create()
    setorDAO.update(setor1)
    setorDAO.update(setor2)


    gerente = Funcionario().Gerente()
    assistente = Funcionario().Assistente()
    requerente = Funcionario().Requerente()
    
    gerente.setStatus("ativo")
    gerente.setSetor("TI")
    assistente.setStatus("ativo")
    assistente.setSetor("TI")
    requerente.setStatus("ativo")


    ### Caso de uso Requisitar Suporte
    listaSetores = SetorMGR.listarSetor()
    listaPrioridade = PedidoMGR.listarPrioridadePedido()
    listaResponse = PedidoMGR.listarResponse()

    pedidoMGR = PedidoMGR()
    pedido = Pedidos(requerente.login, listaSetores[0])
    pedido.setDescrip("Um monitor da sala xxxx precisa ser consertado.")
    pedido.setPriority(listaPrioridade[0])

    # Corrigido: chamado o objeto diretamente
    pedidoMGR.realizarPedidoSuporte(pedido, pedido.setor)

    # Corrigido: chamado o objeto diretamente
    pedidoMGR.validarPedido(pedido, "sim")


if __name__ == "__main__":
    main()
