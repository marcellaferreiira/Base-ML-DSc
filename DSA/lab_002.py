'''
Calculadora para o laboratório 2 - Data science academy
'''

print('------------Python Calculator------------')
operacao = int(input('Selecione a opcão desejada: \n'
                     '1- Adição\n'
                     '2-Subtração\n'
                     '3-Multiplicação\n'
                     '4-Divisão\n'))
while operacao <=4:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input("Digite o segundo número: "))
    if operacao == 1:
        soma = n1 + n2
        print(f'{n1}+{n2}={soma}')
        break
    elif operacao == 2:
        subtracao = n1 - n2
        print(f'{n1}-{n2}={subtracao}')
        print('fim ')
        break
    elif operacao == 3:
        multiplica = n1 * n2
        print(f'{n1}*{n2}={multiplica}')
        print('fim ')
        break
    elif operacao == 4:
        divisao = n1 / n2
        while n1 < n2:
            divisao = n1 / n2
            print('valor inválido, tente novamente')
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input("Digite o segundo número: "))
        if n1 > n2:
            divisao = n1 / n2
            print(f'{n1}/{n2}={divisao}')
            print('fim ')
        break
