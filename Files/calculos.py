import math 
import sys

if len(sys.argv) != 2:
    print("Por favor insira um número")
    sys.exit(1)

number = int(sys.argv[1])

raiz = math.sqrt(number)
fatorial = math.factorial(number)

print(f"A raiz quadrada de: {number} é {raiz} e o fatorial é {fatorial}")

