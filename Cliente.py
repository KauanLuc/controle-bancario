class Cliente:
    def __init__(self, nome, telefone, cpf, lista):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
# lista adiciona o cliente no "banco de dados"
        lista.append(nome)
        lista.append(telefone)
        lista.append(cpf)



