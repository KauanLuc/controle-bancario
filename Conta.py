class Conta:
    def __init__(self, titular, id, saldo, lista):
        self.__titular = titular
        self.__id = id
        self.__saldo = saldo
# lista adiciona a conta no "banco de dados"
        lista.append(titular)
        lista.append(id)

    def _dados(self):
        print('-=-' * 8)
        print(f'DADOS DA CONTA BBK\nTitular: {self.__titular}\nID Cliente: {self.__id}\nSaldo: R${self.__saldo}')
        print('-=-'*8)
    def _saque(self, valor):
        self.valor = valor
        if self.valor > self.__saldo:
            print(f'Saldo Insuficiente para um saque de R${self.valor}.')
        if self.valor <= 0:
            print('Falha. Adicione valor ao saque.')
        else:
            print(f'Saque de R${self.valor} efetuado com sucesso.')
            self.__saldo -= self.valor

    def _deposito(self, deposito):
        self.deposito = deposito
        if self.deposito <= 0:
            print('Falha. Adicione valor ao depósito.')
        else:
            self.__saldo += self.deposito
            print(f'Depósito de R${self.deposito} efetuado com sucesso.')



