from HelpTech.models.cliente import Cliente
from HelpTech.models.funcionario import Funcionario
from HelpTech.models.computador import Computador
from HelpTech.models.celular import Celular
from HelpTech.models.servico import Servico
from HelpTech.models.ordem_servico import OrdemServico
from HelpTech.enums.status_os import StatusOS


# ==========================================
# LISTAS DO SISTEMA
# ==========================================

clientes = []
funcionarios = []
equipamentos = []
ordens = []


# ==========================================
# CADASTRAR CLIENTE
# ==========================================

def cadastrar_cliente():

    print("\n--- CADASTRAR CLIENTE ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")

    cliente = Cliente(nome, cpf, telefone, endereco)

    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso!")


# ==========================================
# LISTAR CLIENTES
# ==========================================

def listar_clientes():

    print("\n--- CLIENTES ---")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:

        print("\n" + cliente.exibir_dados())
        print("-" * 40)


# ==========================================
# CADASTRAR FUNCIONÁRIO
# ==========================================

def cadastrar_funcionario():

    print("\n--- CADASTRAR FUNCIONÁRIO ---")

    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")

    matricula = int(
        input("Matrícula: ")
    )

    especialidade = input(
        "Especialidade: "
    )

    funcionario = Funcionario(
        nome,
        cpf,
        telefone,
        matricula,
        especialidade
    )

    funcionarios.append(funcionario)

    print("\nFuncionário cadastrado com sucesso!")


# ==========================================
# LISTAR FUNCIONÁRIOS
# ==========================================

def listar_funcionarios():

    print("\n--- FUNCIONÁRIOS ---")

    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    for funcionario in funcionarios:

        print("\n" + funcionario.exibir_dados())
        print("-" * 40)


# ==========================================
# CADASTRAR EQUIPAMENTO
# ==========================================

def cadastrar_equipamento():

    print("\n--- CADASTRAR EQUIPAMENTO ---")

    print("1 - Computador")
    print("2 - Celular")

    tipo = input("Escolha: ")

    id_equipamento = len(equipamentos) + 1

    marca = input("Marca: ")
    modelo = input("Modelo: ")
    defeito = input("Defeito: ")

    if tipo == "1":

        processador = input(
            "Processador: "
        )

        equipamento = Computador(
            id_equipamento,
            marca,
            modelo,
            defeito,
            processador
        )

    elif tipo == "2":

        sistema = input(
            "Sistema operacional: "
        )

        equipamento = Celular(
            id_equipamento,
            marca,
            modelo,
            defeito,
            sistema
        )

    else:

        print("\nOpção inválida.")
        return

    equipamentos.append(equipamento)

    print(
        "\nEquipamento cadastrado com sucesso!"
    )


# ==========================================
# LISTAR EQUIPAMENTOS
# ==========================================

def listar_equipamentos():

    print("\n--- EQUIPAMENTOS ---")

    if not equipamentos:
        print("Nenhum equipamento cadastrado.")
        return

    for equipamento in equipamentos:

        print(
            f"\nID: {equipamento.id}"
        )

        print(
            equipamento.descricao()
        )

        print(
            f"Defeito: {equipamento.defeito}"
        )

        print("-" * 40)


# ==========================================
# CRIAR ORDEM DE SERVIÇO
# ==========================================

def criar_ordem():

    print("\n--- NOVA ORDEM DE SERVIÇO ---")

    if not clientes:
        print("Cadastre um cliente primeiro.")
        return

    if not funcionarios:
        print("Cadastre um funcionário primeiro.")
        return

    if not equipamentos:
        print("Cadastre um equipamento primeiro.")
        return

    # CLIENTE

    listar_clientes()

    cpf = input(
        "\nDigite o CPF do cliente: "
    )

    cliente = None

    for item in clientes:

        if item.cpf == cpf:
            cliente = item
            break

    if cliente is None:

        print("Cliente não encontrado.")
        return

    # EQUIPAMENTO

    listar_equipamentos()

    id_equipamento = int(
        input(
            "\nDigite o ID do equipamento: "
        )
    )

    equipamento = None

    for item in equipamentos:

        if item.id == id_equipamento:
            equipamento = item
            break

    if equipamento is None:

        print("Equipamento não encontrado.")
        return

    # FUNCIONÁRIO

    listar_funcionarios()

    matricula = int(
        input(
            "\nDigite a matrícula do funcionário: "
        )
    )

    funcionario = None

    for item in funcionarios:

        if item.matricula == matricula:
            funcionario = item
            break

    if funcionario is None:

        print("Funcionário não encontrado.")
        return

    # SERVIÇO

    print("\n--- SERVIÇO ---")

    descricao = input(
        "Descrição do serviço: "
    )

    valor = float(
        input("Valor do serviço: R$ ")
    )

    servico = Servico(
        descricao,
        valor
    )

    # ORDEM

    ordem = OrdemServico(
        cliente,
        equipamento,
        funcionario,
        servico
    )

    ordens.append(ordem)

    print(
        "\nOrdem de serviço criada!"
    )

    print(
        f"Número da OS: {ordem.numero}"
    )


# ==========================================
# LISTAR ORDENS
# ==========================================

def listar_ordens():

    print("\n--- ORDENS DE SERVIÇO ---")

    if not ordens:

        print(
            "Nenhuma ordem de serviço cadastrada."
        )

        return

    for ordem in ordens:

        print("\n" + ordem.exibir_resumo())

        print("-" * 40)


# ==========================================
# ALTERAR STATUS
# ==========================================

def alterar_status():

    print("\n--- ALTERAR STATUS ---")

    if not ordens:

        print(
            "Nenhuma ordem de serviço cadastrada."
        )

        return

    listar_ordens()

    numero = int(
        input(
            "\nDigite o número da OS: "
        )
    )

    ordem = None

    for item in ordens:

        if item.numero == numero:
            ordem = item
            break

    if ordem is None:

        print("Ordem não encontrada.")
        return

    print("\nNovo status:")

    print("1 - Aberta")
    print("2 - Em andamento")
    print("3 - Finalizada")

    opcao = input("Escolha: ")

    if opcao == "1":

        novo_status = StatusOS.ABERTA

    elif opcao == "2":

        novo_status = StatusOS.EM_ANDAMENTO

    elif opcao == "3":

        novo_status = StatusOS.FINALIZADA

    else:

        print("Opção inválida.")
        return

    ordem.alterar_status(
        novo_status
    )

    print(
        "\nStatus alterado com sucesso!"
    )


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu():

    while True:

        print("\n")
        print("=" * 40)
        print("           HELPTECH")
        print("=" * 40)

        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Cadastrar funcionário")
        print("4 - Listar funcionários")
        print("5 - Cadastrar equipamento")
        print("6 - Listar equipamentos")
        print("7 - Criar ordem de serviço")
        print("8 - Listar ordens de serviço")
        print("9 - Alterar status da OS")
        print("0 - Sair")

        opcao = input(
            "\nEscolha uma opção: "
        )

        if opcao == "1":

            cadastrar_cliente()

        elif opcao == "2":

            listar_clientes()

        elif opcao == "3":

            cadastrar_funcionario()

        elif opcao == "4":

            listar_funcionarios()

        elif opcao == "5":

            cadastrar_equipamento()

        elif opcao == "6":

            listar_equipamentos()

        elif opcao == "7":

            criar_ordem()

        elif opcao == "8":

            listar_ordens()

        elif opcao == "9":

            alterar_status()

        elif opcao == "0":

            print(
                "\nEncerrando o HelpTech..."
            )

            break

        else:

            print(
                "\nOpção inválida."
            )


# ==========================================
# EXECUTAR SISTEMA
# ==========================================

menu()