def validar_lista(lista: list) -> bool:
    """Valida si el dato ingresado es una lista, y de ser así, evalúa si contiene algo o está vacía.

    Args:
        lista (list): espera un dato de tipo lista.

    Returns:
        bool: resultado de la evaluación.
    """
    if isinstance(lista, list):
        return bool(lista)
    else:
        raise ValueError("ERROR, se esperaba una lista.")


def validar_entero(num: int)-> bool:
    if not isinstance(num, int):
        raise ValueError("ERROR, se esperaba un número entero")

def validar_numero(num: int | float)-> bool:
    es_numero = True
    if not isinstance (num, int | float):
        es_numero = False
        raise ValueError("ERROR, el dato ingresado no es un número")
    return es_numero

def validar_campo(lista: list, campo: str) -> None:
    for elem in lista:
        if campo not in elem:
            raise ValueError(f"'{campo}' no es un campo válido para todos los elementos de la lista.")