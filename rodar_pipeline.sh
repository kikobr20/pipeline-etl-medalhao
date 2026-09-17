#!/bin/bash

# 1. Entra na pasta do projeto
cd /home/rodrigo/pipeline-etl-medalhao

# 2. Ativa o ambiente virtual Python
source venv/bin/activate

# 3. Adiciona um carimbo de data e hora no registro
echo "--- Iniciando ETL: $(date) ---"

# 4. Roda as três camadas da Arquitetura Medalhão
python scripts/1_extracao_bronze.py
python scripts/2_transformacao_prata.py
python scripts/3_carga_ouro.py

echo "--- ETL Finalizado com Sucesso ---"