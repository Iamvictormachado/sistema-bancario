menu = """
    ===================== MENU =====================

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Empréstimo
    [0] Sair

    ================================================
    """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Insira o valor do depósiton\n"))
                
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.\n")

    elif opcao == "2":
        valor = float(input("Insira o valor do saque:\n"))
        
        excedeu_limite = valor > limite 
        excedeu_saque = numero_saques >= LIMITE_SAQUES
        excedeu_saldo = valor > saldo


        if excedeu_limite:
            print("Limite insifuciente.\n")

        elif excedeu_saldo:
            print("Saldo insuficiente.\n")

        elif excedeu_saque:
            print("Excedido o limite de 3 saques diários.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.\n")

    elif opcao == "3":
        print("#################### EXTRATO BANCÁRIO ####################\n")
        print("\nNão foram realizadas movimentações na conta."  if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n##########################################################")
        
    elif opcao == "4":
        print("Sem empréstimos disponíveis para você no momento.\n")


    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")