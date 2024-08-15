class funcionarioDAO:
    def __cursorToListOfProduto(self, cursor): # Realiza o SELECT
        row = cursor.fetchone()
        result= []
        while row is not None:
            result.push(self.__rowToProduto(row))
            row = cursor.fetchone()
        return result

    def __rowToProduto(self, row): # Pega os elementos da tabela e separa em variaveis
