import random

# Gera um número aleatório entre 1 e 50
secret = random.randint(1, 50)

# Inicializa o contador de tentativas
tentativas = 0

print("Tente adivinhar o número entre 1 e 50!")

while True:
    try:
        # Solicita um palpite do usuário
        palpite = int(input("Escolha um número entre 1 e 50: "))
        tentativas += 1

        # Verifica se o palpite é maior ou menor que o número secreto
        if palpite < secret:
            print("O número é maior que esse.")
        elif palpite > secret:
            print("O número é menor que esse.")
        else:
            print(f"Parabéns! Você acertou o número {secret} em {tentativas} tentativas!")
            break  # Sai do loop quando o número for adivinhado

    except ValueError:
        print("Por favor, digite um número válido.")
