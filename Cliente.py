import pandas as pd
from sqlalchemy import create_engine

class Cliente:
    def __init__(self, nome, telefone, cpf, lista):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        # criando um dataframe
        dicionario_clientes = {}
        dicionario_clientes['Nome'] = f'{self.nome}'
        dicionario_clientes['Telefone'] = f'{self.telefone}'
        dicionario_clientes['CPF'] = f'{self.cpf}'
        lista.append(dicionario_clientes)
        database_clientes = pd.DataFrame(lista)
        # Conectando ao banco de dados SQLite
        engine = create_engine('sqlite:///Cliente.db')
        # Armazenando o DataFrame como uma tabela SQL
        database_clientes.to_sql(
            'tabela_clientes', engine,
            if_exists='replace', index=False
        )