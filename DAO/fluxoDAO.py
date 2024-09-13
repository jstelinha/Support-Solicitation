from DAO.connect import DBController 


class FluxoDAO:
    def __cursorToListFluxo(self, row):
        connection = DBController().obterConnection()
        cursor = connection.cursor()
        row = cursor.fetchone()

    def __rowToFluxo(self, row):
        fluxo = fluxo()
        fluxo.idPedido = (row['idPedido'])
        fluxo.status = (row['status'])
        fluxo.data = (row['data'])
        return fluxo

    def create(self):
        fluxo = fluxo()
        return fluxo

    def update(self, fluxo):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      if not hasattr(fluxo, 'idPedido'):
        cursor.execute('INSERT INTO fluxo (idPedido, status, data) VALUES(?, ?, ?)',
          fluxo.status, fluxo.data)
      else:
        cursor.execute('UPDATE fluxo SET status=?, data=? WHERE idPedido = ?',
          fluxo.status, fluxo.data)
     
      cursor.close()
      connection.close()
      return True

    def delete(self, fluxo):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      if hasattr(fluxo, 'idPedido'):
        cursor.execute('DELETE FROM fluxo WHERE idPedido = ?', fluxo.idPedido)
        cursor.close()
        connection.close()
        if cursor.rowcount == 0:
          raise "Não foi possível excluir um fluxo com id: " + str(fluxo.idPedido)          
      else:
        cursor.close()
        connection.close()
        raise "Não é possível excluir um fluxo ainda não persistido!"

      return True

    def listFluxoByIds(self, ids):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      cursor.execute('SELECT * FROM pedido WHERE ids = ?', ids)
      
      result = self.__cursorToListFluxo(cursor)
     
      cursor.close()
      connection.close()

      return result