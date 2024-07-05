def validar_lista(lista) -> bool:
    """
    Valida si el dato ingresado es una lista y no está vacía.

    Args:
        lista (list): Dato a evaluar.

    Returns:
        bool: True si es una lista válida y no está vacía, False en caso contrario.
    
    Raises:
        ValueError: Si el dato ingresado no es una lista lanza una excepcion.
    """
    if isinstance(lista, list):
        if len(lista) == 0:
            raise ValueError("La lista está vacía.")
        return True
    else:
        return False

def validar_entero(num: int) -> bool:
    """
    Valida si un dato es un número entero.

    Args:
    - num (int): El dato a validar.

    Raises:
    - ValueError: Si el dato ingresado no es un número entero lanza una excepción.

    Returns:
    - bool: True si el dato es un número entero.
    """
    if not isinstance(num, int):
        raise ValueError("ERROR, se esperaba un número entero")
    return True

def validar_numero(num: int | float) -> bool:
    """
    Valida si un dato es un número (entero o flotante).

    Args:
    - num (int | float): El dato a validar.

    Raises:
    - ValueError: Si el dato ingresado no es ni un entero ni un flotante lanza expeción.

    Returns:
    - bool: True si el dato es un número (entero o flotante).
    """
    if not isinstance(num, (int, float)):
        raise ValueError("ERROR, el dato ingresado no es un número")
    return True

def validar_campo(lista: list, campo: str) -> None:
    """
    Valida si un campo específico está presente en todos los diccionarios de una lista.

    Args:
    - lista (list): Lista de diccionarios a validar.
    - campo (str): Nombre del campo a verificar.

    Raises:
    - ValueError: Si el campo no está presente en al menos un diccionario de la lista.

    Returns:
    - None: La función no retorna ningún valor, pero lanza una excepción si la validación falla.
    """
    for elem in lista:
        if campo not in elem:
            raise ValueError(f"'{campo}' no es un campo válido para todos los elementos de la lista.")

