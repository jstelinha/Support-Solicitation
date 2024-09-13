import mysql.connector
# pip install mysql-connector-python


class DBController:
    def obterConnection(self):
        return mysql.connector.connect(user='APS', password='postgres', host='localhost')
