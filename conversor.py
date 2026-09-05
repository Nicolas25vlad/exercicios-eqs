class ServicoCotacaoIndisponivelError(RuntimeError):
    pass


class ConversorMoedas:
    def __init__(self, cotacao_api):
        self.cotacao_api = cotacao_api

    def converter(self, moeda_origem: str, moeda_destino: str, valor: float) -> float:
        try:
            taxa = self.cotacao_api.obter_taxa(moeda_origem, moeda_destino)
        except Exception as erro:
            raise ServicoCotacaoIndisponivelError("Serviço de cotação indisponível") from erro

        convertido = valor * taxa
        convertido_com_spread = convertido * 1.015
        return round(convertido_com_spread, 2)
