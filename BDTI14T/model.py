import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao() #Abrindo conexao com o banco
        self.db_connection = self.db_connection.conectar()#Metodo que faz a conexao com o DB
        self.con = self.db_connection.cursor() #Navegação no banco de dados; cursor é uma variavel da classe mysql.connector

    def inserir(self, nome, telefone, endereco, dataDeNascimento):
        try:
            sql = "insert into pessoa(codigo, nome, telefone, endereco, dataDeNascimento) values('', '{}', '{}', '{}', '{}')".format(nome, telefone, endereco, dataDeNascimento)
            self.con.execute(sql) #Prepara o dado para ser inserido
            self.db_connection.commit() #Insere o dado no banco
            return "{} linha(s) afetada(s)".format(self.con.rowcount) #Rowcount é uma variavel da classe mysql
        except Exception as erro:
            return erro