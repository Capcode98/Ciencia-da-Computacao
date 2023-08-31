import csv


def media(v1,v2,v3,v4):
    v = v1+v2+v3+v4
    m = v/4
    return m

table_A = []
table_B = []

cabecalho = ["Item","Valor_1","Valor_2","Valor_3","Valor_4","Mercado"]

with open('produtos_s2.csv', 'r+', newline='') as csvfile:

    arquivo = csv.DictReader(csvfile, delimiter=';',fieldnames=cabecalho)

    for row in arquivo:

        if row.get('Mercado') == 'Supermercado_A':

            table_A.append(f'{row.get("Item")};{media(float(row.get("Valor_1")),float(row.get("Valor_2")),float(row.get("Valor_3")),float(row.get("Valor_4")))}')

        if row.get('Mercado') == 'Supermercado_B':

            table_B.append(f'{row.get("Item")};{media(float(row.get("Valor_1")),float(row.get("Valor_2")),float(row.get("Valor_3")),float(row.get("Valor_4")))}')
    
    lista_ordenada_A = sorted(table_A)
    lista_ordenada_B = sorted(table_B)

    for par_ordenado in lista_ordenada_A:

        with open('supermercado_A.csv', "+a") as arquivo_mercado:

            arquivo_mercado.write(f'{par_ordenado}\n')

    for par_ordenado in lista_ordenada_B:

        with open('supermercado_B.csv', "+a") as arquivo_mercado:

            arquivo_mercado.write(f'{par_ordenado}\n')

# MEMBROS DO GRUPO:
# João Luis Berute Ribeiro
# Kauan Vieira Xavier 
# Pedro Henrique
# Lucas Rodrigues
