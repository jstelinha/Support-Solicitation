from DAO.connect import DBController 
from ENTITIES.Pedidos import prioridade, response


class PedidoDAO:
    def __cursorToListPedido(self, row):
        connection = DBController().obterConnection()
        cursor = connection.cursor()
        row = cursor.fetchone()
        result = []
        while row is not None:
          result.push(self.__rowToPedido(row))
          row = cursor.fetchone()
        return result

    def __rowToPedido(self, row):
        pedido = pedido()
        pedido.idPedido = (row['idPedido'])
        pedido.login = (row['login'])
        pedido.desc = (row['desc'])
        pedido.priority = (row['priority'])
        pedido.response = (row['response'])
        return pedido

    def create(self):
        pedido = pedido()
        return pedido

    def update(self, pedido):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      if not hasattr(pedido, 'idPedido'):
        cursor.execute('INSERT INTO pedido (idPedido, login, desc, priority, response, fluxo) VALUES(?, ?, ?, ?)',
          pedido.login, pedido.desc, pedido.priority, pedido.response, pedido.fluxo)
      else:
        cursor.execute('UPDATE pedido SET login=? desc=?, priority=?, response=? WHERE idPedido = ?',
          pedido.login, pedido.desc, pedido.priority, pedido.response)
     
      cursor.close()
      connection.close()
      return True

    def delete(self, pedido):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      if hasattr(pedido, 'idPedido'):
        cursor.execute('DELETE FROM pedido WHERE idPedido = ?', pedido.idPedido)
        cursor.close()
        connection.close()
        if cursor.rowcount == 0:
          raise "Não foi possível excluir um pedido com id: " + str(pedido.idPedido)          
      else:
        cursor.close()
        connection.close()
        raise "Não é possível excluir um pedido ainda não persistido!"

      return True

    def listPedidosById(self, id):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      cursor.execute('SELECT * FROM pedido WHERE idPedido = ?', id)
      
      result = self.__cursorToListPedido(cursor)
     
      cursor.close()
      connection.close()

      return result

    def listPrioridades(self):
      return prioridade.lista()

    def listResponse(self):
       return response.lista()
    