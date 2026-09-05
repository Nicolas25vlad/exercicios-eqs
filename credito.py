def calcular_limite(renda_mensal: float, possui_restricao: bool, score_externo: int) -> float:
    if renda_mensal < 1500 or possui_restricao:
        return 0.0

    limite = renda_mensal * 0.30

    if score_externo > 800:
        limite *= 1.50

    return round(limite, 2)
