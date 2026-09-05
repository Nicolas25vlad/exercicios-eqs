class SaldoInsuficienteError(ValueError):
    pass


class TransacaoInvalidaError(ValueError):
    pass


class Conta:
    def __init__(self):
        self.transacoes = []
        self._proximo_id = 1

    @property
    def saldo(self) -> float:
        total = 0.0
        for transacao in self.transacoes:
            if transacao["status"] != "CONCLUIDO":
                continue
            if transacao["tipo"] == "CREDITO":
                total += transacao["valor"]
            else:
                total -= transacao["valor"]
        return round(total, 2)

    def depositar(self, valor: float) -> dict:
        return self._registrar(valor, "CREDITO")

    def sacar(self, valor: float) -> dict:
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente")
        return self._registrar(valor, "DEBITO")

    def estornar(self, transacao_id: int) -> None:
        for transacao in self.transacoes:
            if transacao["id"] == transacao_id:
                if transacao["status"] != "CONCLUIDO":
                    raise TransacaoInvalidaError("Transação já estornada")
                transacao["status"] = "ESTORNADO"
                return
        raise TransacaoInvalidaError("Transação não encontrada")

    def _registrar(self, valor: float, tipo: str) -> dict:
        transacao = {
            "id": self._proximo_id,
            "valor": valor,
            "tipo": tipo,
            "status": "CONCLUIDO",
        }
        self._proximo_id += 1
        self.transacoes.append(transacao)
        return transacao
