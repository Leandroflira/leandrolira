from mysql.connector import connect

def conexao():
    condb = connect(host = "localhost",
                    user = "root",
                    password = "",
                    database = "comercio")
    return condb