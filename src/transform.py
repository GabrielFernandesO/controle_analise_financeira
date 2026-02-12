"""
transform.py

Responsável por transformar as linhas extraídas do PDF
em um DataFrame estruturado.
"""

import re
import pandas as pd


def transformar_em_dataframe(linhas_transacoes: list) -> pd.DataFrame:
    """
    Recebe as linhas filtradas do PDF e retorna um DataFrame estruturado.
    """

    # Regex detalhada para capturar:
    # - data
    # - descrição
    # - parcela (opcional)
    # - valor
    padrao_extracao = re.compile(
        r"""
        ^\s*
        (?P<data>\d{2}\s+[A-Z]{3})
        .*?
        (?P<descricao>.*?)
        (?:\s+-\s+Parcela\s+(?P<parcela>\d+/\d+))?
        \s+R\$\s+(?P<valor>[\d.,]+)
        $
        """,
        re.VERBOSE
    )

    dados = []

    # Aplica regex em cada linha
    for linha in linhas_transacoes:
        m = padrao_extracao.search(linha)

        if m:
            dados.append({
                "data": m.group("data"),
                "descricao": m.group("descricao").strip(),
                "parcela": m.group("parcela"),
                "valor": float(
                    m.group("valor")
                    .replace(".", "")
                    .replace(",", ".")
                )
            })

    return pd.DataFrame(dados)
