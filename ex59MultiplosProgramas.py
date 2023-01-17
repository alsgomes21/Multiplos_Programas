n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
soma = n1+n2
multiplicacao = n1*n2


print('     [1]SOMAR     ')
print('     [2]MULTIPLICAR     ')
print('     [3]MAIOR     ')
print('     [4] NOVOS NUMEROS     ')
print('     [5]SAIR DO PROGRAMA     ')

opcao = int(input('Qual é a sua opção? '))

if opcao == 1:
    print('A soma de {} + {} = {}'.format(n1,n2,soma))
elif opcao == 2:
    print('A multiplicação de {} x {} = {} '.format(n1,n2,multiplicacao))
elif opcao == 3:
    if n1 > n2:
        print('{} é maior que {}'.format(n1,n2))
    elif n2 > n1:
        print('{} é maior que {}'.format(n2,n1))
elif opcao == 4:
    int(input('Digite um novo número '))
    int(input('Digite outro número: '))

    print('     [1]SOMAR     ')
    print('     [2]MULTIPLICAR     ')
    print('     [3]MAIOR     ')
    print('     [4] NOVOS NUMEROS     ')
    print('     [5]SAIR DO PROGRAMA     ')

    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        print('A soma de {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        print('A multiplicação de {} x {} = {} '.format(n1, n2, multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
    elif opcao == 4:
        int(input('Digite um novo número '))
        int(input('Digite outro número: '))
    elif opcao == 5:
        print('Sair do programa')
elif opcao == 5:
    print('Sair do programa')
