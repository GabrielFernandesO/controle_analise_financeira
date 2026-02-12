"""
modeling.py

Responsável por aplicar modelos de Machine Learning.

"""

from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np


def detectar_anomalias(df):
    """
    Aplica Isolation Forest para identificar gastos fora do padrão.

    Retorna o DataFrame com nova coluna:
    - anomalia (1 = normal, -1 = anomalia)
    """

    # Selecionamos features numéricas relevantes
    features = df[[
        "valor",
        "dia_semana",
        "fim_de_semana"
    ]]

    # Inicializa modelo
    modelo = IsolationForest(
        n_estimators=100,
        contamination=0.05,  # 5% dos dados serão considerados anomalias
        random_state=42
    )

    # Treina modelo
    modelo.fit(features)

    # Predição
    df["anomalia"] = modelo.predict(features)

    return df

def clusterizar_comportamento(df):
    """
    Aplica KMeans para identificar padrões de comportamento financeiro.

    Retorna:
    - DataFrame com nova coluna 'cluster'
    """

    # Selecionamos variáveis numéricas relevantes
    features = df[[
        "valor",
        "fim_de_semana",
        "dia_semana"
    ]]

    # Padronização 
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Modelo KMeans
    modelo = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    df["cluster"] = modelo.fit_predict(features_scaled)

    return df

def prever_gastos(df):
    """
    Cria modelo simples de regressão linear para prever tendência de gastos.
    """

    # Ordena por data
    df = df.sort_values("data_completa")

    # Criamos variável temporal numérica
    df["tempo_index"] = np.arange(len(df))

    X = df[["tempo_index"]]
    y = df["valor"]

    modelo = LinearRegression()
    modelo.fit(X, y)

    # Previsão dentro da base
    df["valor_previsto"] = modelo.predict(X)

    return df