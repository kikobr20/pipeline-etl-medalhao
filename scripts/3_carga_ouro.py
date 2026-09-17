import os
import glob
import pandas as pd
import sqlite3

# 1. Encontra o arquivo CSV mais recente na pasta Prata
arquivos_prata = glob.glob("data/prata/youtube_busca_*.csv")
if not arquivos_prata:
    print("Nenhum arquivo encontrado na pasta Prata. Rode a transformação primeiro.")
    exit()

arquivo_recente = max(arquivos_prata, key=os.path.getctime)
print(f"Processando arquivo para a Camada Ouro: {arquivo_recente}")

# 2. Carrega os dados limpos
df_prata = pd.read_csv(arquivo_recente)

# 3. Modelagem de Dados (Camada Ouro)
# Vamos extrair o ano de publicação para facilitar agrupamentos nas consultas SQL
df_prata['ano_publicacao'] = pd.to_datetime(df_prata['data_publicacao']).dt.year

# 4. Conexão com o Banco de Dados SQLite (Nosso Data Warehouse local)
caminho_banco = "data/ouro/youtube_analytics.db"
conexao = sqlite3.connect(caminho_banco)

# 5. Carga de Dados (Load)
# Salvamos o DataFrame diretamente como uma tabela SQL chamada 'dim_videos'
df_prata.to_sql("dim_videos", conexao, if_exists="replace", index=False)

conexao.close()
print(f"Sucesso! Dados inseridos na tabela 'dim_videos' do banco em: {caminho_banco}")