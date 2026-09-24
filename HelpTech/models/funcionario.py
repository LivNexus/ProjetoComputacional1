from .pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(
        self,
        nome,
        cpf,
        telefone,
        matricula,
        especialidade
    ):
        super().__init__(
            nome,
            cpf,
            telefone
        )

        self.matricula = matricula
        self.especialidade = especialidade

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, valor):
        if valor <= 0:
            raise ValueError(
                "A matrícula deve ser positiva."
            )

        self._matricula = valor

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, valor):
        if not valor.strip():
            raise ValueError(
                "A especialidade não pode ser vazia."
            )

        self._especialidade = valor.strip()

    def exibir_dados(self):
        return (
            f"Funcionário: {self.nome}\n"
            f"Matrícula: {self.matricula}\n"
            f"Especialidade: {self.especialidade}"
        )