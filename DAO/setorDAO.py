from connect import DBController 


class setorDAO:
    def __cursorToListProduto(self, row):
        connection = DBController().obterConnection()
        cursor = connection.cursor()
        row = cursor.fetchone()

    def __rowToProduto(self, row):
        setor = setor()
        setor.ids = (row['ids'])
        setor.nome = (row['nome'])
        setor.pedidos = (row['pedidos'])
        return setor

    def create(self):
        setor = setor()
        return setor
    
    def update(self, setor:object):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      if not hasattr(setor, 'ids'):
        cursor.execute('INSERT INTO setor (ids, nome, pedidos) VALUES(?, ?)',
          setor.ids, setor.pedidos, setor.nome)

      else:
        cursor.execute('UPDATE setor SET nome=?, pedidos=? WHERE ids = ?',
          setor.nome, setor.pedidos, setor.ids)
     
      cursor.close()
      connection.close()
      return True

    def delete(self, setor:object):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      if hasattr(setor, 'ids'):
        cursor.execute('DELETE FROM setor WHERE id = ?', setor.ids)
        cursor.close()
        connection.close()
        if cursor.rowcount == 0:
          raise "Não foi possível excluir um setor com id: " + str(setor.ids)          
      else:
        cursor.close()
        connection.close()
        raise "Não é possível excluir um setor ainda não persistido!"

      return True

    def listByNome(self, nome):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      cursor.execute('SELECT * FROM setor WHERE nome = ?', nome)
      
      result = self.__cursorToListOfProduto(cursor)
     
      cursor.close()
      connection.close()

      return result