import sys

if len(sys.argv) != 3:
    print("Por favor insira dois números")
    sys.exit(1)

number1 = float(sys.argv[1])
number2 = float(sys.argv[2])

response = number1 + number2

print(f"A soma entre {number1} e {number2} é: {response}")

