from datetime import datetime

def menu():
    return input("""\n
    ===== MENU =====
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta corrente
    [6] Listar contas
    [0] Sair
    => """)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f"[{agora}] Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo


def sacar(*, saldo, valor, extrato, limite, saques, max_saques):
    if valor <= 0:
        print("Valor inválido para saque.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Limite de saque excedido.")
    elif saques >= max_saques:
        print("Limite diário de saques excedido.")
    else:
        saldo -= valor
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f"[{agora}] Saque: R$ {valor:.2f}")
        saques += 1
        print("Saque realizado com sucesso!")
    return saldo, saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO =====")
    if extrato:
        for op in extrato:
            print(op)
    else:
        print("Nenhuma movimentação.")
    print(f"Saldo atual: R$ {saldo:.2f}")


def filtrar_usuario(usuarios, cpf):
    return next((u for u in usuarios if u["cpf"] == cpf), None)


def criar_usuario(usuarios):
    raw = input("CPF (somente números ou formatado): ")
    cpf = "".join(filter(str.isdigit, raw))
    if filtrar_usuario(usuarios, cpf):
        print("Usuário já existe com esse CPF.")
        return
    nome = input("Nome completo: ")
    nasc = input("Data de nascimento (dd-mm-aaaa): ")
    end = input("Endereço: ")
    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "nascimento": nasc,
        "endereco": end
    })
    print("Usuário criado com sucesso!")


def criar_conta_corrente(contas, usuarios, agencia):
    raw = input("CPF do titular (somente dígitos ou formatado): ")
    cpf = "".join(filter(str.isdigit, raw))
    usuario = filtrar_usuario(usuarios, cpf)
    if not usuario:
        print("Usuário não encontrado.")
        return
    numero = len(contas) + 1 
    contas.append({
        "agencia": agencia,
        "numero": numero,
        "usuario": usuario
    })
    print("Conta corrente criada com sucesso!")

def listar_contas(contas):
    print("\n===== CONTAS CADASTRADAS =====")
    if not contas:
        print("Nenhuma conta registrada.")
    for c in contas:
        print(f"Agência: {c['agencia']} | Conta: {c['numero']} | Titular: {c['usuario']['nome']}")

def main():
    saldo = 0.0
    extrato = []
    limite = 500.0
    saques = 0
    max_saques = 3
    agencia = "0001"
    usuarios = []  
    contas   = [] 

    while True:
        opc = menu()

        if opc == "1":
            valor = float(input("Valor para depósito: "))
            saldo = depositar(saldo, valor, extrato)

        elif opc == "2":
            valor = float(input("Valor para saque: "))
            saldo, saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                saques=saques,
                max_saques=max_saques
            )

        elif opc == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opc == "4":
            criar_usuario(usuarios)

        elif opc == "5":
            criar_conta_corrente(contas, usuarios, agencia)

        elif opc == "6":
            listar_contas(contas)

        elif opc == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
