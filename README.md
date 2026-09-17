# ⚙️ Pipeline ETL - API do YouTube (Arquitetura Medalhão)

Este projeto é um pipeline de Engenharia de Dados completo desenvolvido em Python. Ele realiza a extração de dados da API oficial do YouTube, transforma os dados estruturando-os de forma limpa e os carrega em um Data Warehouse local (SQLite), seguindo o padrão de mercado da **Arquitetura Medalhão** (Bronze, Prata e Ouro).

## 🏗️ Arquitetura do Projeto

O fluxo de dados foi desenhado para garantir rastreabilidade e qualidade da informação em cada etapa:

1. **🥉 Camada Bronze (Raw):** 
   - Script: `1_extracao_bronze.py`
   - O pipeline consome a YouTube Data API v3 buscando métricas de vídeos sobre "Engenharia de Dados".
   - Os dados são salvos em seu estado bruto original no formato `.json`.
   
2. **🥈 Camada Prata (Cleansed):** 
   - Script: `2_transformacao_prata.py`
   - Leitura do JSON mais recente. Acontece o "achatamento" (flattening) dos dados aninhados.
   - Utilização do **Pandas** para limpeza de caracteres especiais, tipagem de datas (datetime) e remoção de dados nulos.
   - Exportação do dado estruturado em formato `.csv`.

3. **🥇 Camada Ouro (Curated):** 
   - Script: `3_carga_ouro.py`
   - Ingestão do CSV limpo.
   - Modelagem de dados para criação de tabelas dimensão.
   - Carga (Load) em um banco de dados relacional **SQLite** (`.db`), pronto para consumo por ferramentas de BI ou Cientistas de Dados.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Manipulação de Dados:** Pandas
* **Banco de Dados:** SQLite
* **APIs:** YouTube Data API v3 / `requests`
* **Gerenciamento de Ambiente:** `venv` / `python-dotenv`

## 🚀 Como executar este projeto

1. Clone o repositório:
```bash
git clone git@github.com:kikobr20/pipeline-etl-medalhao.git
cd pipeline-etl-medalhao