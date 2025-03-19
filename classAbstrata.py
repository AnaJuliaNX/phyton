from abc import ABC, abstractmethod

# crio umna class abstrata
class Animal(ABC):
    def falar(self):
       return print("Fa som")

# subclass com criação do método cor
class Gato(Animal):
    def falar(self):
        return print("Maiu Miau")
    
    def cor(self):
        return print("A cor do gato é laranja")
        
# subclass com criação do método nome
class Cachorro(Animal):
    def falar(self):
        return print("Au Au")
    
    def nome(self):
       return print("O cachorro chama Vomitilda")
    

gato = Gato()
cachorro = Cachorro()

gato.falar()
gato.cor()
cachorro.falar()
cachorro.nome()