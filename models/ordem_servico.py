from enums.status_os import StatusOS

class OrdemServico:

    _proximo_numero = 1

    def __init__(self, cliente, equipamento, funcionario, servico):
        self.numero = OrdemServico._proximo_numero
        OrdemServico._proximo_numero += 1

        self.cliente = cliente
        self.equipamento = equipamento
        self.funcionario = funcionario
        self.servico = servico

        self.status = StatusOS.ABERTA

    @property
    def total(self):
        return self.servico.calcular_valor()

    def alterar_status(self, novo_status):
        self.status = novo_status

    def exibir_resumo(self):
        return (
            f"OS: #{self.numero}\n"
            f"Cliente: {self.cliente.nome}\n"
            f"Equipamento: "
            f"{self.equipamento.marca} "
            f"{self.equipamento.modelo}\n"
            f"Funcionário: "
            f"{self.funcionario.nome}\n"
            f"Serviço: "
            f"{self.servico.descricao}\n"
            f"Valor: R$ {self.total:.2f}\n"
            f"Status: {self.status.value}"
        )