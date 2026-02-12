"""
main.py

Arquivo principal do projeto.

Responsável por:
1. Orquestrar todo o fluxo do sistema
2. Chamar os módulos corretos
3. Garantir que as etapas sejam executadas na ordem certa

"""

import os
import shutil

# =========================
# IMPORTAÇÃO DOS MÓDULOS
# =========================

from src.extract import (
    obter_pdf_unico,
    extrair_linhas_transacoes,
    identificar_mes
)

from src.features import (
    criar_features_temporais,
    criar_features_financeiras,
    criar_features_categoria
)

from src.modeling import (
    detectar_anomalias,
    clusterizar_comportamento,
    prever_gastos
)

from src.visualize import (
    salvar_grafico_clusters,
    salvar_grafico_previsao
)

from src.modeling import detectar_anomalias
from src.transform import transformar_em_dataframe
from src.categorize import classificar_gasto
from src.analysis import resumo_por_categoria, resumo_por_dia
from src.visualize import salvar_grafico_categoria, salvar_grafico_dia
from src.visualize import salvar_grafico_anomalias
from src.export import exportar_excel, adicionar_dashboard_excel


def main():
    """
    Função principal que executa todo o pipeline:
    Extração → Transformação → Análise → Visualização → Exportação
    """

    print("Iniciando processamento da fatura...\n")

    # =========================
    # 1 DEFINIR PASTAS
    # =========================

    pasta_entrada = "Faturas_Entrada"
    pasta_backup = "Faturas_Entrada_bkp"

    # =========================
    # 2 EXTRAÇÃO
    # =========================

    # Obtém o único PDF presente na pasta
    caminho_pdf = obter_pdf_unico(pasta_entrada)

    # Extrai apenas as linhas que representam transações
    linhas_transacoes = extrair_linhas_transacoes(caminho_pdf)

    # Identifica o mês da fatura
    mes_fatura = identificar_mes(linhas_transacoes)

    print(f"Fatura identificada como mês: {mes_fatura.upper()}")

    # =========================
    # 3 PREPARAR DIRETÓRIO DE SAÍDA
    # =========================

    diretorio_saida = f"Faturas_Processadas/{mes_fatura.upper()}"
    os.makedirs(diretorio_saida, exist_ok=True)

    # =========================
    # 4 TRANSFORMAÇÃO
    # =========================

    df = transformar_em_dataframe(linhas_transacoes)

    # Classificação de categorias
    df["categoria"] = df["descricao"].apply(classificar_gasto)

    print("Transformação concluída.")

    # =========================
    # 4.1 FEATURE ENGINEERING
    # =========================

    df = criar_features_temporais(df)
    df = criar_features_financeiras(df)
    df = criar_features_categoria(df)

    # =========================
    # 4.2 DETECÇÃO DE ANOMALIAS
    # =========================

    df = detectar_anomalias(df)

    print("Detecção de anomalias concluída.")

    # =========================
    # 4.3 CLUSTERIZAÇÃO
    # =========================
    df = clusterizar_comportamento(df)
    print("Clusterização concluída.")

    # =========================
    # 4.4 PREVISÃO
    # =========================
    df = prever_gastos(df)
    print("Previsão de gastos concluída.")


    # =========================
    # 5 ANÁLISE
    # =========================

    gastos_categoria, df_categoria = resumo_por_categoria(df)
    gastos_dia = resumo_por_dia(df)

    print("Análises realizadas.")

    # =========================
    # 6 VISUALIZAÇÃO
    # =========================

    caminho_img_categoria = f"{diretorio_saida}/grafico_categoria.png"
    caminho_img_dia = f"{diretorio_saida}/grafico_dia.png"
    caminho_img_anomalia = f"{diretorio_saida}/grafico_anomalias.png"
    caminho_img_previsao = f"{diretorio_saida}/grafico_previsao.png"
    caminho_img_cluster = f"{diretorio_saida}/grafico_clusters.png"

    salvar_grafico_categoria(gastos_categoria, caminho_img_categoria)
    salvar_grafico_dia(gastos_dia, caminho_img_dia)
    salvar_grafico_anomalias(df, caminho_img_anomalia)
    salvar_grafico_clusters(df, caminho_img_cluster)
    salvar_grafico_previsao(df, caminho_img_previsao)

    print("Gráficos gerados.")

    # =========================
    # 7 EXPORTAÇÃO PARA EXCEL
    # =========================

    arquivo_excel = f"{diretorio_saida}/dashboard_financeiro.xlsx"

    exportar_excel(df, df_categoria, arquivo_excel)
    adicionar_dashboard_excel(
        arquivo_excel,
        caminho_img_categoria,
        caminho_img_dia
    )

    print("Excel com dashboard criado.")

    # =========================
    # 8 BACKUP DO PDF PROCESSADO
    # =========================

    shutil.move(caminho_pdf, pasta_backup)

    print("Arquivo movido para backup.")
    print("\nProcessamento finalizado com sucesso! 🚀")




# =========================
# EXECUÇÃO DO PROGRAMA
# =========================

if __name__ == "__main__":
    main()
