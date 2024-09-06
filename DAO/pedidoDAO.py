from connect import DBController 


class pedidoDAO:
    def __cursorToListProduto(self, row):
        connection = DBController().obterConnection()
        cursor = connection.cursor()
        row = cursor.fetchone()

    def __rowToProduto(self, row):
        pedido = pedido()
        pedido.ids = (row['ids'])
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

      if not hasattr(pedido, 'id'):
        cursor.execute('INSERT INTO pedido (ids, desc, priority, response) VALUES(?, ?, ?, ?)',
          pedido.ids, pedido.desc, pedido.priority, pedido.response)
      else:
        cursor.execute('UPDATE pedido SET desc=?, priority=?, response=? WHERE ids = ?',
          pedido.ids, pedido.desc, pedido.priority, pedido.response)
     
      cursor.close()
      connection.close()
      return True

    def delete(self, pedido):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      if hasattr(pedido, 'id'):
        cursor.execute('DELETE FROM pedido WHERE ids = ?', pedido.id)
        cursor.close()
        connection.close()
        if cursor.rowcount == 0:
          raise "Não foi possível excluir um pedido com id: " + str(pedido.id)          
      else:
        cursor.close()
        connection.close()
        raise "Não é possível excluir um pedido ainda não persistido!"

      return True

    def listByNome(self, nome):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      cursor.execute('SELECT * FROM pedido WHERE nome = ?', nome)
      
      result = self.__cursorToListOfProduto(cursor)
     
      cursor.close()
      connection.close()

      return result
