from connect import DBController 


class setorDAO:
    def __cursorToListSetor(self, row):
        connection = DBController().obterConnection()
        cursor = connection.cursor()
        row = cursor.fetchone()
        result = []
        while row is not None:
          result.push(self.__rowToSetor(row))
          row = cursor.fetchone()
        return result

    def __rowToSetor(self, row):
        setor = setor()
        setor.idSetor = (row['idSetor'])
        setor.nome = (row['nome'])
        setor.pedidos = (row['pedidos'])
        return setor

    def create(self):
        setor = setor()
        return setor
    
    def update(self, setor):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      if not hasattr(setor, 'ids'):
        cursor.execute('INSERT INTO setor (idSetor, nome, pedidos) VALUES(?, ?)',
          setor.pedidos, setor.nome)

      else:
        cursor.execute('UPDATE setor SET nome=?, pedidos=? WHERE idSetor = ?',
          setor.nome, setor.pedidos, setor.idSetor)
     
      cursor.close()
      connection.close()
      return True

    def delete(self, setor:object):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      if hasattr(setor, 'idSetor'):
        cursor.execute('DELETE FROM setor WHERE idSetor = ?', setor.idSetor)
        cursor.close()
        connection.close()
        if cursor.rowcount == 0:
          raise "Não foi possível excluir um setor com idSetor: " + str(setor.idSetor)          
      else:
        cursor.close()
        connection.close()
        raise "Não é possível excluir um setor ainda não persistido!"

      return True

    def listaSetores(self):
        connection = DBController().obterConnection();
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM setor')

        result = self.__cursorToListSetor(cursor)

        cursor.close()
        connection.close()

        return result

    def listPedidoById(self, id):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      cursor.execute('SELECT pedido FROM setor WHERE id = ?', id)
      
      result = self.__cursorToListSetor(cursor)
     
      cursor.close()
      connection.close()

      return result

    def listRelatorio(self):
      connection = DBController().obterConnection();
      cursor = connection.cursor()

      cursor.execute('SELECT * FROM setor')
      
      result = self.__cursorToListSetor(cursor)
     
      cursor.close()
      connection.close()

      return result
    