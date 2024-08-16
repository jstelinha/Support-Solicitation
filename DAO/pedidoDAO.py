from connect import __connect 


class pedidoDAO:
    def __cursorToListProduto(self, row):
        connection = __connect()
        cursor = connection.cursor()
        row = cursor.fetchone()

    def __rowToProduto(self, row):
        pedido = pedido()
        pedido.ids = (row['ids'])
        pedido.desc = (row['desc'])
        pedido.priority = (row['priority'])
        pedido.response = (row(['response']))
        return pedido

    def create(self):
        pedido = pedido()
        return pedido
    
    def update(self):
        connection = __connect()
        cursor = connection.cursor()

        cursor.execute(""" """)

        cursor.close()
        connection.close()

    def delete(self):
        return None
