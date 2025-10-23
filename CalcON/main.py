import test

number1 = int(input('Escolha um número: '))
number2 = int(input('Escolha um outro número: '))

def soma():
    print(f'{number1 + number2}')

def subtracao():
    print(f'{number1 - number2}')

def divisao():
    print(f'{number1 / number2}')

def multiplicacao():
    print(f'{number1 * number2}')

escolha = input('Escolha o Operador: (+, -, /, *): ')

if escolha == '+':
    soma()

elif escolha == '-':
    subtracao()

elif escolha == '/':
    divisao()

elif escolha == '*':
    multiplicacao()

else:
    print('Escolha um operador válido e tente novamente!')