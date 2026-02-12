"""
extract.py

Responsável por:
1. Localizar o PDF da pasta de entrada
2. Ler o PDF
3. Identificar páginas que contenham "TRANSAÇÕES"
4. Extrair as linhas relevantes com regex
5. Identificar o mês da fatura
"""

import os
import re
import pdfplumber


def obter_pdf_unico(pasta_entrada: str) -> str:
    """
    Verifica se existe exatamente um PDF na pasta.
    Retorna o caminho completo do arquivo.
    """

    arquivos_pdf = [
        f for f in os.listdir(pasta_entrada)
        if f.lower().endswith(".pdf")
    ]

    if len(arquivos_pdf) != 1:
        raise ValueError("A pasta deve conter exatamente um arquivo PDF.")

    return os.path.join(pasta_entrada, arquivos_pdf[0])


def extrair_linhas_transacoes(caminho_pdf: str) -> list:
    """
    Abre o PDF e retorna apenas as linhas que representam transações.
    """

    paginas_transacoes = []

    # Abre o PDF
    with pdfplumber.open(caminho_pdf) as pdf:
        for page in pdf.pages:
            texto = page.extract_text()

            # Só pega páginas que contenham a palavra TRANSAÇÕES
            if texto and "TRANSAÇÕES" in texto:
                paginas_transacoes.append(texto)

    # Regex para identificar linhas válidas de transação
    padrao_transacao = re.compile(r"^\s*\d{2} [A-Z]{3} .*••••.* R\$")

    linhas_transacoes = []

    for texto in paginas_transacoes:
        for linha in texto.split("\n"):
            if padrao_transacao.search(linha):
                linhas_transacoes.append(linha.strip())

    return linhas_transacoes


def identificar_mes(linhas_transacoes: list) -> str:
    """
    Identifica o mês da fatura com base na primeira transação encontrada.
    """

    if not linhas_transacoes:
        return "mes"

    m = re.search(r"^\s*\d{2}\s+([A-Z]{3})", linhas_transacoes[0])

    return m.group(1).lower() if m else "mes"
