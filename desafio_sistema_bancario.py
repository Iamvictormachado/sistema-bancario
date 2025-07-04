import textwrap

def menu():
    menu = """\n
    ===================== MENU =====================

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCriar usuário
    [5]\tAbrir conta
    [6]\tListar contas
    [9]\tEmpréstimo
    [i]\tInstruções
    [0]\tSair

    ================================================
    \n"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.\n")
    return saldo, extrato

def saque(*, extrato, valor, limite, numero_saques, limite_saques, saldo):
    excedeu_limite = valor > limite 
    excedeu_saque = numero_saques >= limite_saques
    excedeu_saldo = valor > saldo
    
    if excedeu_limite:
        print("\nLimite insifuciente.")

    elif excedeu_saldo:
        print("\nSaldo insuficiente.")

    elif excedeu_saque:
        print("\nExcedido o limite de 3 saques diários.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR${valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
  
    else:
        print("Operação falhou! O valor informado é inválido.\n")

    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("#################### EXTRATO BANCÁRIO ####################\n")
    print("\nNão foram realizadas movimentações na conta."  if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n##########################################################")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números):> ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\Conta criada com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, voltando ao menu...")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

    #return print("Nenhuma conta criada até o momento.")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números):> ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return
    
    nome = input("Informe seu nome completo:> ")
    data_nascimento = input("Informe sua data de nascimento (DIA-MÊS-ANO):> ")
    endereco = input("Informe o seu endereço (logadouro, número - bairro - cidade / sigla estado):> ")
    
    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n\n\tUsuário criado com sucesso!")

#def solicitar_emprestimo():


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    emprestimo = 5000


    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Insira o valor do depósito:> \n"))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("Insira o valor do saque:> \n"))
            
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            extrato(saldo, extrato=extrato)
        
        elif opcao == "5":
            criar_usuario(usuarios)
        
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "9":
            print("Sem empréstimos disponíveis para você no momento.\n")

        elif opcao == "i":
            print("#################### PASSO-A-PASSO ####################\n")
            print("Instruções para abrir uma conta no banco DIO.")
            print("É necessário abrir uma conta!")
            print("Após abrir a conta, você deverá criar um usuário.")
            print("Através de uma conta aberta, você pode criar diversos usuários.")
            print("Todos os usuários portarão a mesma agência.")
            print("\n##########################################################")

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
