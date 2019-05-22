from pymysql import *

class connection:
    def connection(self):
        conn = connect('127.0.0.1', 'root', '', 'project')
        return conn