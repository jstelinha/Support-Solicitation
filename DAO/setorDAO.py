from connect import __connect 


class setorDAO:
    def __cursorToListProduto(self, row):
        connection = __connect()
        cursor = connection.cursor()
        row = cursor.fetchone()

    def __rowToProduto(self, row):
        setor = setor()
        setor.ids = (row['ids'])
        setor.nome = (row['nome'])
        return setor

    def create(self):
        setor = setor()
        return setor
    
    def update(self):
        connection = __connect()
        cursor = connection.cursor()

        cursor.execute(""" """)

        cursor.close()
        connection.close()

    def delete(self):
        return None
