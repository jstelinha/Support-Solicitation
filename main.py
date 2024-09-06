from ENTITIES.funcionario import funcionario
from ENTITIES.pedido import pedido 
from ENTITIES.fPedido import fPedido  
from ENTITIES.setor import setor 
from MGR.setorMGR import setorMGR
from MGR.pedidoMGR import pedidoMGR 
from DAO.pedidoDAO import pedidoDAO 
from DAO.setorDAO import setorDAO
from DVO.pedidoDVO import pedidoDVO 
from DVO.setorDVO import setorDVO
from connect import __connect


def main():
    conexao = __connect("host_name", "user_name", "user_password")
    
    gerente = funcionario().gerente()
    assistente = funcionario().assistente()
    requerente = funcionario().requerente()
    assistenteF = funcionario().assistente()

    pedidoEmergencia = pedido()
    pedidoBaixo = pedido()
    pedidoEmergencia.setDescrip("Um monitor da sala xxxx precisa ser consertado.")
    pedidoBaixo.setDescrip("Um bebedouro da sala xxxx não está funcionando mais.")
    pedidoEmergencia.setPriority("eMergencia")
    pedidoBaixo.setPriority("Baixo")

    gerente.setStatus("ativo")
    assistente.setStatus("ativo")
    requerente.setStatus("ativo")
    assistenteF.setStatus("ferias")

    setor1 = setor("TI")
    setor2 = setor("Manutenção predial")

    pedidoMGR.requisitarSuporte(pedidoEmergencia(), setor1())
    pedidoMGR.requisitarSuporte(pedidoBaixo(), setor2())
    pedidoMGR.validarPedido(pedidoEmergencia(), "sim")
    pedidoMGR.validarPedido(pedidoBaixo(), "nao")

main()
