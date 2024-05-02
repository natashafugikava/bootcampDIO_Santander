depositos = []
saques = []
saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3

while True:
    opcao = str(input('''Escolha uma opção:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ''')).lower()

    if opcao == 'd':
        print('Depósito')
        valor = float(input('Quando deseja depositar? '))
        if valor > 0:
            print(f'R$ {valor:.2f} depositado na conta.')
            depositos.append(valor)
            saldo += valor
        else:
            print('Valor inválido, tente novamente.')
            
    if opcao == 's':
        print('Saque')
        valor = float(input('Quando deseja sacar? '))
        if valor > 0 and valor <= 500:
            if numero_saques < limite_saques:
                if valor <= saldo:
                    numero_saques += 1
                    saques.append(valor)
                    saldo -= valor
                    print(f'R$ {valor:.2f} sacados com êxito.')
                else:
                    print('Não há saldo suficiente.')
            else:
                print('Número de saques máximo alcançado.')
        else:
            print(f'O valor do saque precisa ser positivo e no máximo R$ {limite:.2f}.')
            
    if opcao == 'e':
        print('Extrato')
        print('Depósitos:')
        for i in depositos:
            print(f'R$ {i:.2f}')
        print('Saques:')
        for i in saques:
            print(f'R$ {i:.2f}')            
        print(f'Saldo atual: R$ {saldo:.2f}')
        
    if opcao == 'q':
        break