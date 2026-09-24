from .pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(
        self,
        nome,
        cpf,
        telefone,
        endereco
    ):
        super().__init__(
            nome,
            cpf,
            telefone
        )

        self.endereco = endereco

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor):
        if not valor.strip():
            raise ValueError(
                "O endereço não pode ser vazio."
            )

        self._endereco = valor.strip()

    def exibir_dados(self):
        return (
            f"Cliente: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Telefone: {self.telefone}\n"
            f"Endereço: {self.endereco}"
        )