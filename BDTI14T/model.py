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

    def selecionar(self):
        try:
            sql = "select * from pessoa"
            self.con.execute(sql)#Devolve os dados salvos
            msg = ""
            for(codigo, nome, telefone, endereco, dataDeNascimento) in self.con:
                msg += "\nCoódigo: {}, Nome: {}, Telefone: {}, Endereço: {}, Data de Nascimento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
            return msg
        except Exception as erro:
            return erro

    def atualizar(self, campo, novoDado, cod):
        try:
            sql = "update pessoa set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha(s) atualizada(s)!".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def excluir(self, cod):
        try:
            sql = "delete from pessoa where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            print("{} linha(s) excluída(s)!".format(self.con.rowcount))
        except Exception as erro:
            return erro
