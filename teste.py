class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado.")
        else:
            print("Valor inválido.")

    def ver_saldo(self):
        print(f"Saldo: {self.__saldo}")


# Criando um objeto
conta = ContaBancaria("João", 1000)

# Tentando acessar o saldo diretamente (não funciona)
print(conta._ContaBancaria__saldo)  # Erro! Atributo privado.

# Usando métodos para interagir com o saldo
conta.depositar(500)
conta.ver_saldo()  # Saída: Saldo: 1500