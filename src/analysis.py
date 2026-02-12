"""
analysis.py

Responsável por gerar análises agregadas:
- Resumo por categoria
- Resumo por dia
"""


def resumo_por_categoria(df):
    """
    Agrupa os dados por categoria e soma os valores.
    """

    gastos_categoria = (
        df.groupby("categoria")["valor"]
        .sum()
        .sort_values(ascending=False)
    )

    df_categoria = gastos_categoria.to_frame("Total")

    # Adiciona linha TOTAL
    total_geral = df_categoria["Total"].sum()
    df_categoria.loc["TOTAL"] = total_geral

    return gastos_categoria, df_categoria


def resumo_por_dia(df):
    """
    Agrupa os dados por data e soma os valores.
    """
    return df.groupby("data")["valor"].sum()
