# Classe Pai
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome 
        self.idade = idade 
        self.endereco = endereco

    def mostrarDados(self):
        print(f'Pessoa: {self.nome}, {self.idade}, {self.endereco}') 

# Herança da classe pai com adição de atributo
class Funcionario(Pessoa):
    def __init__(self, nome, idade, endereco, salario):
        self.nome = nome 
        self.idade = idade
        self.endereco = endereco 
        self.salario = salario 

    def mostrarTudo(self):
         print(f'Pessoa: {self.nome}, {self.idade}, {self.endereco}, {self.salario}') 


pessoa_um = Pessoa("Ana", 20, "Rua das Histórias não contadas")

pessoa_um.mostrarDados()