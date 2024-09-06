from connect import DBController 


class fluxoDAO:
    def __cursorToListFluxo(self, row):
        connection = DBController().obterConnection()
        cursor = connection.cursor()
        row = cursor.fetchone()

    def __rowToFluxo(self, row):
        fluxo = fluxo()
        fluxo.ids = (row['ids'])
        fluxo.status = (row['status'])
        fluxo.data = (row['data'])
        return fluxo

    def create(self):
        fluxo = fluxo()
        return fluxo

    def update(self, fluxo):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      if not hasattr(fluxo, 'ids'):
        cursor.execute('INSERT INTO fluxo (ids, status, data) VALUES(?, ?, ?)',
          fluxo.ids, fluxo.status, fluxo.data)
      else:
        cursor.execute('UPDATE fluxo SET status=?, data=? WHERE ids = ?',
          fluxo.status, fluxo.data, fluxo.ids)
     
      cursor.close()
      connection.close()
      return True

    def delete(self, fluxo):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      if hasattr(fluxo, 'ids'):
        cursor.execute('DELETE FROM fluxo WHERE ids = ?', fluxo.ids)
        cursor.close()
        connection.close()
        if cursor.rowcount == 0:
          raise "Não foi possível excluir um fluxo com id: " + str(fluxo.ids)          
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