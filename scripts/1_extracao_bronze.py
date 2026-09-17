import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

# 1. Carrega a chave de API do arquivo .env
load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')

# TESTE: Verificando se a chave está chegando
print(f"Chave lida do .env: {API_KEY}")
# 2. Configura a requisição para a API do YouTube
# Vamos buscar os 50 vídeos mais relevantes sobre "Engenharia de Dados"
URL = "https://www.googleapis.com/youtube/v3/search"
parametros = {
        "part": "snippet",
        "q": "Engenharia de Dados",
        "type": "video",
        "maxResults": 50,
        "key": API_KEY
}

print("Iniciando extração de dados do YouTube...")
resposta = requests.get(URL, params=parametros)

# 3. Verifica se a requisição deu certo (Código 200 significa OK)
if resposta.status_code == 200:
        dados_brutos = resposta.json()
        
        # 4. Gera um timestamp para não sobrescrever extrações antigas
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho_arquivo = f"data/bronze/youtube_busca_{timestamp}.json"
        
        # 5. Salva o JSON bruto na nossa pasta Bronze
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
                json.dump(dados_brutos, arquivo, ensure_ascii=False, indent=4)
                
        print(f"Sucesso! Dados brutos salvos em: {caminho_arquivo}")
else:
        print(f"Erro na requisição. Código HTTP: {resposta.status_code}")
        print(resposta.text)