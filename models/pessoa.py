from abc import ABC, abstractmethod


class Pessoa(ABC):

    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("O nome não pode ser vazio.")

        self._nome = valor.strip()

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        if not valor.strip():
            raise ValueError("O CPF não pode ser vazio.")

        self._cpf = valor.strip()

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor.strip()

    @abstractmethod
    def exibir_dados(self):
        pass