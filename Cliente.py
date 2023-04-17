class Cliente:
    def __init__(self, nome, telefone, cpf, lista):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
# lista adiciona o cliente no "banco de dados"
        dicionario_clientes = {}
        dicionario_clientes['Nome'] = f'{self.nome}'
        dicionario_clientes['Telefone'] = f'{self.telefone}'
        dicionario_clientes['CPF'] = f'{self.cpf}'
        lista.append(dicionario_clientes)
