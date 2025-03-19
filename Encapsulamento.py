class Produto:
    def __init__(self, nome, preco):
        self.set_nome(nome)  # Usando setter para validar o nome
        self.set_preco(preco)  # Usando setter para validar o preço

    # Getter para o atributo nome
    def get_nome(self):
        return self.__nome

    # Setter para o atributo nome
    def set_nome(self, nome):
        if nome.strip() == "":  # Validando se não é uma string vazia
            raise ValueError("O nome não pode ser em branco")
        self.__nome = nome

    # Getter para o atributo preco
    def get_preco(self):
        return self.__preco

    # Setter para o atributo preco
    def set_preco(self, preco):
        if preco <= 0:  # Validando se o valor é maior que zero
            raise ValueError("O preço não pode ser 0 ou negativo")
        self.__preco = preco

    # Método para exibir o retorno
    def mostrar(self):
        return f"Produto: {self.__nome}, custa: R$ {self.__preco:.2f}"
    
    # Método __str__ para imprimir a instância diretamente
    def __str__(self):
        return self.mostrar()

# Preenchendo os valores 
produto = Produto("Livro", 59.90)
print(produto.mostrar())  # Saída: Produto: Livro, custa: R$ 59.90

# Tentando criar um produto sem nome
try:
    prodSemNome = Produto("", 32.50)
except ValueError as e:
    print(e)  # Saída: O nome não pode ser em branco

# Tentando criar um produto com preço inválido
try:
    prodSemPreco = Produto("Caneta", 0)
except ValueError as e:
    print(e)  # Saída: O preço não pode ser 0 ou negativo

# Modificando os atributos com setter
prodSemNome = Produto("Vela aromática", 50.00)  # Produto válido
prodSemPreco = Produto("Caneta", 3.50)  # Produto válido
print(prodSemNome)  # Usando o __str__ que chama o método mostrar
print(prodSemPreco)  # Usando o __str__ que chama o método mostrar
