from DAO.connect import DBController
from ENTITIES.Setor import Setor


class SetorDAO:
    def __cursorToListSetor(self, cursor):
        result = []
        row = cursor.fetchone()
        while row is not None:
            result.append(self.__rowToSetor(row))
            row = cursor.fetchone()
        return result

    def __rowToSetor(self, row):
        stor = Setor()
        stor.idSetor = row['idSetor']
        stor.nome = row['nome']
        stor.pedidos = row['pedidos']
        return stor

    def create(self):
        return Setor()

    def update(self, setor: object):
        connection = DBController().obterConnection()
        cursor = connection.cursor()

        if not hasattr(setor, 'idSetor'):
            cursor.execute(
                'INSERT INTO setor (nome, pedidos) VALUES(?, ?)',
                (setor.nome, setor.pedidos)
            )
        else:
            cursor.execute(
                'UPDATE setor SET nome=?, pedidos=? WHERE idSetor=?',
                (setor.nome, setor.pedidos, setor.idSetor)
            )

        connection.commit()
        cursor.close()
        connection.close()
        return True

    def delete(self, setor: object):
        connection = DBController().obterConnection()
        cursor = connection.cursor()

        if hasattr(setor, 'idSetor'):
            cursor.execute('DELETE FROM setor WHERE idSetor = ?', (setor.idSetor,))
            if cursor.rowcount == 0:
                raise Exception(f"Não foi possível excluir um setor com idSetor: {setor.idSetor}")
        else:
            cursor.close()
            connection.close()
            raise Exception("Não é possível excluir um setor ainda não persistido!")

        connection.commit()
        cursor.close()
        connection.close()
        return True

    def listaSetores(self):
        connection = DBController().obterConnection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM setor')
        result = self.__cursorToListSetor(cursor)

        cursor.close()
        connection.close()

        return result

    def listPedidoById(self, id):
        connection = DBController().obterConnection()
        cursor = connection.cursor()

        cursor.execute('SELECT pedido FROM setor WHERE id = ?', (id,))
        result = self.__cursorToListSetor(cursor)

        cursor.close()
        connection.close()

        return result

    def listRelatorio(self):
        connection = DBController().obterConnection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM setor')
        result = self.__cursorToListSetor(cursor)

        cursor.close()
        connection.close()

        return result
