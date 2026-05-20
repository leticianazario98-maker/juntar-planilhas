import pandas as pd
import os

PASTA_PLANILHAS = "planilhas"
ARQUIVO_FINAL = "planilha_final.xlsx"

arquivos = [
    arq for arq in os.listdir(PASTA_PLANILHAS)
    if arq.endswith(".xlsx")
]

dfs = []

for arquivo in arquivos:
    caminho = os.path.join(PASTA_PLANILHAS, arquivo)

    df = pd.read_excel(caminho)

    df["arquivo_origem"] = arquivo

    dfs.append(df)

resultado = pd.concat(dfs, ignore_index=True)

resultado.to_excel(ARQUIVO_FINAL, index=False)

print("Planilha criada com sucesso.")
