from model import model

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("\n\nEscolha umas das opções abaixo:\n\n" +
                "0. Sair\n" +
                "1. Cadastrar\n" +
                "2. Consultar\n" +
                "3. Atualizar\n" +
                "4. Excluir")
        self.setOpcao(int(input()))

    def cadastrar(self):
        print("Informe o seu nome:")
        nome = input()
        print("Informe o seu telefone:")
        telefone = input()
        print("Informe o seu endereco:")
        endereco = input()
        print("Informe o seu data de nascimento:")
        dataDeNascimento = input()
        print(self.modelo.inserir(nome, telefone, endereco, dataDeNascimento))

    def operacoes(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                self.cadastrar()

            else:
                print("Opção inválida! Tente novamente.")
