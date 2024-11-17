import pandas as pd
import datetime
import calendar
import random
import numpy as np
import locale

locale.setlocale(locale.LC_ALL,"Portuguese")

# =======================================================================================================================
def colunas_categoricas(lista_possiveis_valores,datas):
    lista = []
    numero_linhas = len(datas)
    for nlinha in range(numero_linhas):
        lista.append(random.choice(lista_possiveis_valores))
    return lista
        
def colunas_valores(lista_produtos, datas):
    lista=[]
    limites_minimos={}
    numero_linhas=len(datas)   
    itens_distintos = list(dict.fromkeys(lista_produtos))
    # montar uma tabela dimensão com o valor mínimo pra cada produto, aleatoriamente entre 50 e 300
    for i in range(len(itens_distintos)):
        limites_minimos[itens_distintos[i]] = random.randint(50,300)
    # calcular valores aleatórios entre o valor de cada item na tabela dimensão e 120% seu valor
    for i in range(numero_linhas):
        lista.append(random.randint(limites_minimos[lista_produtos[i]],int(limites_minimos[lista_produtos[i]]*1.2)))
    return lista    
    
def colunas_quantidades(datas):
    lista=[]
    numero_linhas=len(datas)
    for linha in range(numero_linhas):
        lista.append(random.randint(150,1000))
    return lista        

# =======================================================================================================================
# Montar coluna com datas: começando em 01/07/2024, 5 linhas por dia, até o último dia do mês anterior à data de hoje
# =======================================================================================================================
datas=[]
data = datetime.date(2024,7,1)

mes=0
while data < datetime.date(datetime.date.today().year, datetime.date.today().month, 1):
    for i in range(calendar.monthrange(data.year,data.month)[1]):
        for n in range(5):
            datas.append(data)
            n+=1
        if data.day == calendar.monthrange(data.year,data.month)[1]:
            continue
        data = datetime.date(data.year,data.month,data.day+1)    
    i+=1
    data = datetime.date(data.year,data.month+1,1)    
# =======================================================================================================================
# Chamar as funções definidas no começo
# =======================================================================================================================
col_linha_producao = colunas_categoricas(['Linha A', 'Linha B', 'Linha C'],datas)
col_produto = colunas_categoricas(['SportComfy', 'High Society', 'Casuality'],datas)
col_unidades_produzidas = colunas_quantidades(datas)
col_defeitos = [int(np.floor(i*(random.randint(1,10))/100)) for i in col_unidades_produzidas]
col_turnos = colunas_categoricas(['Manhã','Tarde','Noite'],datas)
col_fabrica = colunas_categoricas(['São Paulo','Rio de Janeiro','Belo Horizonte'],datas)
col_custo = colunas_valores(col_produto,datas)

df=pd.DataFrame({'Data':datas,'Linha de produção': col_linha_producao, 'Produto': col_produto,
                 'Unidades produzidas': col_unidades_produzidas, 'Defeitos': col_defeitos,
                 'Turno': col_turnos, 'Fábrica': col_fabrica, 'Custo de aquisição': col_custo})

df.loc[df['Produto']=='Casuality','Unidades produzidas'] = df['Unidades produzidas'] * 1.8
df.loc[df['Linha de produção']=='Linha B','Defeitos'] = df['Defeitos'] * 2
df.loc[df['Fábrica']=='Rio de Janeiro','Defeitos'] = df['Defeitos'] * 1.7

for data in df['Data'].astype(str).str[:7].drop_duplicates():
    df_mes=df[df['Data'].astype(str).str[:7]==data]
    df_mes.to_excel(f'Planilha_producao_{data[-2:]}-{data[:4]}.xlsx',index=None)