def menu():
    return input("""\n
    ===== MENU =====
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair
    => """)


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")
    return saldo


def sacar(saldo, valor, extrato, limite, saques, max_saques):
    if valor <= 0:
        print("Valor inválido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Limite excedido.")
    elif saques >= max_saques:
        print("Limite de saques excedido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques += 1
        print("Saque realizado com sucesso!")
    return saldo, saques


def exibir_extrato(saldo, extrato):
    print("\n===== EXTRATO =====")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Nenhuma movimentação.")
    print(f"Saldo atual: R$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("CPF: ")
    if any(u["cpf"] == cpf for u in usuarios):
        print("Usuário já existe.")
        return
    nome = input("Nome completo: ")
    nascimento = input("Nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço: ")
    usuarios.append({"nome": nome, "cpf": cpf, "nascimento": nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")


def criar_conta(contas, usuarios, agencia):
    cpf = input("CPF do titular: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if not usuario:
        print("Usuário não encontrado.")
        return
    numero = len(contas) + 1
    contas.append({"agencia": agencia, "numero": numero, "titular": usuario["nome"]})
    print("Conta criada com sucesso!")


def listar_contas(contas):
    for c in contas:
        print(f"\nAgência: {c['agencia']}\nConta: {c['numero']}\nTitular: {c['titular']}")


def main():
    saldo = 0
    extrato = []
    limite = 500
    saques = 0
    max_saques = 3
    agencia = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Valor do depósito: "))
            saldo = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Valor do saque: "))
            saldo, saques = sacar(saldo, valor, extrato, limite, saques, max_saques)

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            criar_conta(contas, usuarios, agencia)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


main()
