"""
categorize.py

Responsável por classificar os gastos com base na descrição da transação.
Cada gasto recebe uma categoria definida por regras simples (if/else).
"""


def classificar_gasto(descricao: str) -> str:
    """
    Recebe a descrição da transação e retorna a categoria correspondente.
    """

    # Converte para minúsculo
    d = descricao.lower()

    # =========================
    # REGRAS DE CLASSIFICAÇÃO
    # =========================

    if "uber" in d or "99 ride" in d or "dl*99" in d or "pg *99" in d:
        return "Transporte"

    if "99food" in d or "restaurante" in d or "mc " in d:
        return "Alimentação"

    if "supermercado" in d or "mercearia" in d:
        return "Mercado"

    if "spotify" in d or "gympass" in d or "wellhub" in d or "netflix" in d or "barbeariabestbarbe" in d:
        return "Assinaturas"

    if "drogaria" in d or "farmacia" in d:
        return "Saúde"

    if "shopee" in d or "mercadolivre" in d or "casasbahia" in d:
        return "Compras"

    # Caso não encaixe em nenhuma regra
    return "Outros"
