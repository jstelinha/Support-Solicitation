import mysql.connector
# pip install mysql-connector-python


class DBController:
    def obterConnection(self):
        return mysql.connector.connect(user='if0_37164897', password='sz3FKlnrhUGEE', host='sql110.byetcluster.com')
