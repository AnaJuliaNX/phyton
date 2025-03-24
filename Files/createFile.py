import os 

#Crio minha pasta
os.makedirs("meus_arquivos", exist_ok=True)

# Crio meu arquivo dentro da pasta
path_file = os.path.join('meus_arquivos', 'dados.txt')

# Escrevo alguma coisa dentro do arquivo
with open(path_file, 'w') as arquivo:
    arquivo.write('Olha aqui que legal')

# Printo a pasta que foi criado 
print(f'Arquivo criado em: {path_file}')

# Printo minhas pastas desse diretório
print(os.listdir('.'))
