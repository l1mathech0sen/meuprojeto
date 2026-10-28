adms = [{"nome": "Lucas", "email": "admteste@gmail.com", "senha": "123"}]
clientes = []
dentistas = []
salas = []
consultas = []


def cadastrar_cliente():
    print("\n=== CADASTRAMENTO DE CLIENTE ===")
    nome = input("Insira seu nome: ")
    cpf = input("Insira seu CPF: ").strip()

    if not cpf.isdigit() or len(cpf) != 11:
        print("O CPF deve conter exatamente 11 números.")
        return

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("Esse CPF já está cadastrado.")
            return

    novo_cliente = {
        "nome": nome,
        "cpf": cpf
    }

    clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    print("\n=== CLIENTES CADASTRADOS ===")

    if len(clientes) == 0:
        print("Ainda não há clientes cadastrados.")
        return

    for cliente in clientes:
        print("Nome:", cliente["nome"])
        print("CPF:", cliente["cpf"])
        print("--------------------")

def cadastro_dentistas():
    print("\n=== CADASTRO DE DENTISTA ===")

    nome = input("Nome do dentista: ")
    especialidade = input("Especialidade: ")

    for dentista in dentistas:
        if dentista["especialidade"] == especialidade:
            print("Essa especialidade já está ocupada.")
            return

    novo_dentista = {
        "id": len(dentistas) + 1,
        "nome": nome,
        "especialidade": especialidade
    }

    dentistas.append(novo_dentista)
    print("Dentista cadastrado com sucesso!")


def listar_dentistas():
    print("\n=== DENTISTAS CADASTRADOS ===")

    if len(dentistas) == 0:
        print("Ainda não há dentistas cadastrados.")
        return

    for dentista in dentistas:
        print("ID:", dentista["id"])
        print("Nome:", dentista["nome"])
        print("Especialidade:", dentista["especialidade"])
        print("--------------------")


def painel_adm(adm):
    while True:
        print("\n=== PAINEL DE ADMINISTRAÇÃO ===")
        print("1 - Cadastrar clientes")
        print("2 - Listar clientes")
        print("3 - Cadastrar dentista")
        print("4 - Listar dentistas")
        print("0 - Sair")

        opcao = input("Escolha uma opção abaixo: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            cadastro_dentistas()
        elif opcao == "4":
            listar_dentistas()
        elif opcao == "0":
            print("Você saiu da sua conta.")
            return
        else:
            print("Opção inválida.")


def login_adm():
    print("=== LOGIN DO ADMINISTRADOR ===")
    email = input("E-mail: ")
    senha = input("Senha: ")

    for adm in adms:
        if adm["email"] == email and adm["senha"] == senha:
            print("Bem-vindo,", adm["nome"])
            painel_adm(adm)
            return

    print("E-mail ou senha incorretos.")

def menu_inicial():
    while True:
        print("\n=== CLÍNICA ODONTOLÓGICA ===")
        print("1 - Paciente")
        print("2 - Administração")
        print("0 - Encerrar programa")

        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("O painel do paciente será desenvolvido.")
        elif opcao == "2":
            login_adm(adms)
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")

login_adm()