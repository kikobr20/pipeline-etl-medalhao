import os
import json
import pandas as pd
import glob

# 1. Encontra o arquivo JSON mais recente na pasta Bronze
arquivos_bronze = glob.glob("data/bronze/youtube_busca_*.json")
if not arquivos_bronze:
    print("Nenhum arquivo encontrado na pasta Bronze. Rode a extração primeiro.")
    exit()

# Pega o último arquivo gerado
arquivo_recente = max(arquivos_bronze, key=os.path.getctime)
print(f"Processando arquivo: {arquivo_recente}")

# 2. Carrega os dados brutos
with open(arquivo_recente, "r", encoding="utf-8") as f:
    dados_brutos = json.load(f)

# 3. Lista para armazenar apenas os dados que importam
videos_limpos = []

# Navega dentro da estrutura complexa do JSON do YouTube
for item in dados_brutos.get('items', []):
    snippet = item.get('snippet', {})
    
    # Extrai o ID do vídeo (necessário para buscar views e likes depois)
    id_video = item.get('id', {}).get('videoId')
    
    # Ignora canais ou playlists (queremos apenas vídeos)
    if not id_video:
        continue
        
    video = {
        'id_video': id_video,
        'titulo': snippet.get('title'),
        'id_canal': snippet.get('channelId'),
        'nome_canal': snippet.get('channelTitle'),
        'data_publicacao': snippet.get('publishedAt'),
        'descricao': snippet.get('description')
    }
    videos_limpos.append(video)

# 4. Transforma a lista limpa em um DataFrame do Pandas
df = pd.DataFrame(videos_limpos)

# 5. Tratamento de Dados com Pandas (Camada Prata)
# Remove caracteres especiais (como quebras de linha) que podem quebrar o CSV
df['titulo'] = df['titulo'].str.replace(r'[\n\r]', ' ', regex=True).str.strip()
df['descricao'] = df['descricao'].str.replace(r'[\n\r]', ' ', regex=True).str.strip()

# Converte a data de string para o formato datetime do Pandas (Padrão UTC)
df['data_publicacao'] = pd.to_datetime(df['data_publicacao'])

# Remove registros defeituosos
df = df.dropna(subset=['titulo'])

# 6. Salva o resultado estruturado na pasta Prata
caminho_prata = arquivo_recente.replace('bronze', 'prata').replace('.json', '.csv')
df.to_csv(caminho_prata, index=False, encoding='utf-8')

print(f"Sucesso! {len(df)} vídeos processados e salvos em: {caminho_prata}")