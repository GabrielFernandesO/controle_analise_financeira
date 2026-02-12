"""
visualize.py

Responsável por gerar e salvar gráficos.
"""

import matplotlib.pyplot as plt


def salvar_grafico_categoria(gastos_categoria, caminho_saida):
    """
    Gera gráfico de barras de gastos por categoria.
    """

    plt.figure(figsize=(8, 5))
    gastos_categoria.plot(kind="bar")
    plt.title("Gastos por categoria")
    plt.ylabel("Valor (R$)")
    plt.xlabel("Categoria")
    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=150)
    plt.close()


def salvar_grafico_dia(gastos_dia, caminho_saida):
    """
    Gera gráfico de linha de gastos ao longo do mês.
    """

    plt.figure(figsize=(8, 5))
    gastos_dia.plot(marker="o")
    plt.title("Gastos ao longo do mês")
    plt.ylabel("Valor (R$)")
    plt.xlabel("Data")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=150)
    plt.close()


def salvar_grafico_anomalias(df, caminho_saida):
    """
    Gera gráfico destacando gastos anômalos.
    """

    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 5))

    normais = df[df["anomalia"] == 1]
    anomalias = df[df["anomalia"] == -1]

    plt.scatter(normais["data_completa"], normais["valor"])
    plt.scatter(anomalias["data_completa"], anomalias["valor"])

    plt.title("Detecção de Anomalias")
    plt.xlabel("Data")
    plt.ylabel("Valor (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(caminho_saida, dpi=150)
    plt.close()


def salvar_grafico_clusters(df, caminho_saida):
    """
    Gera gráfico mostrando clusters de comportamento.
    """

    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 5))

    for cluster in df["cluster"].unique():
        dados_cluster = df[df["cluster"] == cluster]
        plt.scatter(
            dados_cluster["data_completa"],
            dados_cluster["valor"]
        )

    plt.title("Clusterização de Comportamento")
    plt.xlabel("Data")
    plt.ylabel("Valor (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(caminho_saida, dpi=150)
    plt.close()


def salvar_grafico_previsao(df, caminho_saida):
    """
    Plota valores reais vs previstos.
    """

    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 5))

    plt.plot(df["data_completa"], df["valor"])
    plt.plot(df["data_completa"], df["valor_previsto"])

    plt.title("Previsão de Gastos")
    plt.xlabel("Data")
    plt.ylabel("Valor (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(caminho_saida, dpi=150)
    plt.close()