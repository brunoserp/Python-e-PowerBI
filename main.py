import pandas as pd
import polars as pl
import os

pasta=r'C:\Users\bserpellone\Desktop\Python\github\Python e Power BI'
df_concat = pd.DataFrame()
for file in os.listdir(pasta):
    if file.endswith('xlsx'):
        df = pl.read_excel(os.path.join(pasta,file))
        df = df.to_pandas()
        # adicionar coluna UF
        df.loc[df['Fábrica']=='São Paulo','UF'] = 'SP'
        df.loc[df['Fábrica']=='Belo Horizonte','UF'] = 'MG'
        df.loc[df['Fábrica']=='Rio de Janeiro','UF'] = 'RJ'

        df_concat = pd.concat(objs=[df_concat,df])
    
df_concat[['Unidades produzidas','Defeitos','Custo de aquisição']] = df_concat[['Unidades produzidas','Defeitos','Custo de aquisição']].astype(int)
        



