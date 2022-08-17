import pandas as pd
# pandas
# openpyxl
#twilio
# Passo a passo solução

# Abrir os 6 arquivos excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:

    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas  = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f"no mês {mes} bateu a meta: Vendedor {vendedor}, Vendas: {vendas}")


# Pra cada Arquivo verificar se algum valor na coluna vendas é masio que 55.000

# Se for maior que 55.000 -> Enviar SMS com o nome, o m~es e as vendas do vendedor

# Caso não seja maior que 55.000 não faça nada
