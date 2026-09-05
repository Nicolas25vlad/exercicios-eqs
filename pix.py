import re
import uuid


class ChavePixInvalidaError(ValueError):
    pass


def _validar_cpf(cpf: str) -> bool:
    if not cpf.isdigit() or len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    numeros = [int(n) for n in cpf]

    soma = sum(numeros[i] * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    soma = sum(numeros[i] * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    return numeros[9] == digito1 and numeros[10] == digito2


def identificar_chave_pix(chave: str) -> str:
    if _validar_cpf(chave):
        return "CPF"

    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", chave):
        return "EMAIL"

    if re.fullmatch(r"\+55\d{11}", chave):
        return "TELEFONE"

    try:
        valor = uuid.UUID(chave)
        if valor.version == 4 and str(valor) == chave.lower():
            return "EVP"
    except ValueError:
        pass

    raise ChavePixInvalidaError("Chave Pix inválida")
