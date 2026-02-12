"""
features.py

Responsável por criar novas variáveis (feature engineering)
para enriquecer os dados e permitir modelagem futura.
"""

import pandas as pd
import numpy as np


def criar_features_temporais(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria colunas baseadas em data:
    - dia_num
    - mes_num
    - dia_semana
    - fim_de_semana
    """

    # Extrai o número do dia (primeiros 2 caracteres)
    df["dia_num"] = df["data"].str[:2].astype(int)

    # Mapeamento de mês texto -> número
    mapa_meses = {
        "JAN": 1, "FEV": 2, "MAR": 3, "ABR": 4,
        "MAI": 5, "JUN": 6, "JUL": 7, "AGO": 8,
        "SET": 9, "OUT": 10, "NOV": 11, "DEZ": 12
    }

    df["mes_str"] = df["data"].str[3:6]
    df["mes_num"] = df["mes_str"].map(mapa_meses)

    # Criar uma data real (ano fixo por enquanto)
    df["data_completa"] = pd.to_datetime(
        "2025-" +
        df["mes_num"].astype(str) + "-" +
        df["dia_num"].astype(str),
        errors="coerce"
    )

    # Dia da semana (0 = segunda, 6 = domingo)
    df["dia_semana"] = df["data_completa"].dt.dayofweek

    # Flag fim de semana
    df["fim_de_semana"] = df["dia_semana"].apply(
        lambda x: 1 if x >= 5 else 0
    )

    return df


def criar_features_financeiras(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria métricas financeiras:
    - gasto acumulado
    - zscore do valor
    """

    # Ordena por data
    df = df.sort_values("data_completa")

    # Gasto acumulado no mês
    df["gasto_acumulado"] = df["valor"].cumsum()

    # Z-Score (detecção de outlier)
    df["valor_zscore"] = (
        (df["valor"] - df["valor"].mean()) /
        df["valor"].std()
    )

    return df


def criar_features_categoria(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria métricas relacionadas às categorias:
    - proporção do gasto por categoria
    """

    total_mes = df["valor"].sum()

    gasto_por_categoria = (
        df.groupby("categoria")["valor"]
        .transform("sum")
    )

    df["proporcao_categoria"] = gasto_por_categoria / total_mes

    return df
