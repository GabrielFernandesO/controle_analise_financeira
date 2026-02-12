# 📊 Controle e Análise Financeira

Sistema automatizado de análise comportamental financeira a partir de
faturas de cartão de crédito (Nubank), aplicando **ETL, Feature
Engineering e Machine Learning** para geração de insights e modelagem de
padrões de consumo.

------------------------------------------------------------------------

## 🎥 Demonstração do Projeto

📌 **Video explicação and walkthrough:**\
👉 *\[Coloque aqui o link do vídeo demonstrando o projeto\]*

------------------------------------------------------------------------

## 🚀 Project Overview

Este projeto realiza automaticamente:

-   📥 Extração de dados a partir de PDF
-   🧹 Limpeza e transformação de dados
-   🏷 Classificação automática de gastos
-   🧠 Feature engineering
-   🚨 Detecção de anomalias
-   🎯 Clusterização de comportamento financeiro
-   📈 Previsão de tendência de gastos
-   📊 Geração de dashboard em Excel

------------------------------------------------------------------------

## 🏗 Arquitetura do Projeto

    Controle_Financeiro/
    │
    ├── src/
    │   ├── extract.py
    │   ├── transform.py
    │   ├── categorize.py
    │   ├── features.py
    │   ├── analysis.py
    │   ├── modeling.py
    │   ├── visualize.py
    │   └── export.py
    │
    ├── Faturas_Entrada/
    ├── Faturas_Processadas/
    ├── Faturas_Entrada_bkp/
    │
    └── main.py

------------------------------------------------------------------------

## 🔄 Data Pipeline

### 1️⃣ Extraction (ETL)

-   PDF parsing com `pdfplumber`
-   Regex para identificação das transações
-   Identificação automática do mês da fatura

### 2️⃣ Data Transformation

-   Conversão para DataFrame
-   Padronização de valores
-   Estruturação de colunas

### 3️⃣ Feature Engineering

Variáveis criadas: - Dia numérico - Mês numérico - Data completa - Dia
da semana - Flag de fim de semana - Gasto acumulado - Z-score -
Proporção por categoria

------------------------------------------------------------------------

## 🤖 Machine Learning

### 🚨 Anomaly Detection

Modelo: **Isolation Forest**\
Objetivo: Identificar gastos fora do padrão normal de consumo.

### 🎯 Behavioral Clustering

Modelo: **KMeans**\
Segmentação de padrões de comportamento financeiro.

### 📈 Spending Forecast

Modelo: **Linear Regression**\
Modelagem da tendência temporal dos gastos.

------------------------------------------------------------------------

## 🛠 Tecnologias usadas

-   Python
-   Pandas
-   Scikit-Learn
-   Matplotlib
-   PDFPlumber
-   OpenPyXL

------------------------------------------------------------------------

## ▶️ Como executar

1.  Coloque a fatura PDF na pasta:

```{=html}
<!-- -->
```
    Faturas_Entrada/

2.  Execute:

``` bash
python main.py
```

3.  Os resultados serão gerados automaticamente em:

```{=html}
<!-- -->
```
    Faturas_Processadas/

------------------------------------------------------------------------

## 🎯 Skills

-   Data Extraction (ETL)
-   Data Cleaning & Transformation
-   Feature Engineering
-   Unsupervised Learning (KMeans)
-   Anomaly Detection (Isolation Forest)
-   Regression Modeling
-   Modular Project Architecture
-   Automated Reporting

------------------------------------------------------------------------

## 👨‍💻 Autor

Projeto desenvolvido para portfólio em Data Science.

Por Gabriel Fernandes de Oliveira
