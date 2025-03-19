#classe pai
class Veiculo:
    def __init__(self, tipo, modelo):
        self.tipo = tipo
        self.modelo = modelo

    def descrever(self):
        raise NotImplementedError("Devem implementar esse método")
    
# herda a classe pai 
class Carro(Veiculo):
    def __init__(self, tipo, marca, placa, modelo):
        self.tipo = tipo
        self.marca = marca
        self.placa = placa
        self.modelo = modelo

    def descrever(self):
        return print(f'Esse é o: {self.tipo}, {self.marca}, {self.placa}, {self.modelo}')
    
class Bicicleta(Veiculo):
    def __init__(self, tipo, modelo, acessorio, aro):
        self.tipo = tipo
        self.modelo = modelo
        self.acessorio = acessorio
        self.aro = aro

    def descrever(self):
        return print(f'Esse é: {self.tipo}, {self.modelo}, {self.acessorio}, {self.aro}')
    

carro = Carro("Carro", "Ford", "AQU1", "Mustang")
bicicleta = Bicicleta("Bike", "Caloi", "Garrafa", 18)

print(carro.descrever())
print(bicicleta.descrever())