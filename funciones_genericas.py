from validaciones import *
from os import system

''' PROMEDIO '''
def totalizar_lista(lista: list) -> float:
    """
    Calcula la suma total de los elementos en una lista.

    Args:
    - lista (list): Lista de elementos numéricos.

    Returns:
    - float: Suma total de los elementos en la lista.
    """
    validar_lista(lista)
    total = 0
    for elem in lista:
        total += elem
    return total

def calcular_promedio(lista: list) -> float:
    """
    Calcula el promedio de los elementos en una lista.

    Args:
    - lista (list): Lista de elementos numéricos.

    Returns:
    - float: Promedio de los elementos en la lista.
    """
    validar_lista(lista)
    tam = len(lista)
    total = totalizar_lista(lista)
    promedio = total / tam
    return promedio

def promediar_listas(lista_a: list, lista_b: list, lista_promedios: list) -> None:
    """
    Calcula el promedio de los elementos en dos listas y los guarda en una tercera lista.

    Args:
    - lista_a (list): Primera lista de elementos numéricos.
    - lista_b (list): Segunda lista de elementos numéricos.
    - lista_promedios (list): Lista donde se guardarán los promedios resultantes.

    Returns:
    - None
    """
    for i in range(len(lista_a)):
        promedio = (lista_a[i] + lista_b[i]) / 2
        lista_promedios.append(promedio)

''' FILTRO '''
def filtrar(lista: list, campo: str, dato) -> list:
    """
    Filtra los elementos de una lista basado en un valor específico en un campo dado.

    Args:
    - lista (list): Lista de diccionarios.
    - campo (str): Nombre del campo en el que se realizará la búsqueda.
    - dato: Valor a buscar en el campo especificado.

    Returns:
    - list: Lista filtrada que contiene solo los elementos que cumplen con la condición de búsqueda.
    """
    lista_filtrada = []
    for elem in lista:
        if elem[campo] == dato:
            lista_filtrada.append(elem)
    return lista_filtrada

''' IMPRESIONES '''
def mostrar_lista(lista: list) -> None: 
    """
    Muestra los elementos de una lista en la consola.

    Args:
    - lista (list): Lista de elementos.

    Returns:
    - None
    """
    for elem in lista:
        print(f'id: {elem['id_bike']} \n'
              f'nombre: {elem['nombre']} \n'
              f'tipo: {elem['tipo']} \n'
              f'tiempo: {elem['tiempo']} \n')

def mostrar_diccionario(diccionario: dict) -> None:
    """
    Muestra los elementos de un diccionario en la consola.

    Args:
    - diccionario (dict): Diccionario a mostrar.

    Returns:
    - None
    """
    for key in diccionario:
        print(f"{key}: {diccionario[key]}")

''' MÁXIMOS Y MÍNIMOS '''
def calcular_maximo(lista: list) -> int:
    """
    Encuentra el valor máximo en una lista de elementos numéricos.

    Args:
    - lista (list): Lista de elementos numéricos.

    Returns:
    - int: Valor máximo en la lista.
    """
    validar_lista(lista)
    maximo = lista[0] 
    for elemento in lista:
        if maximo < elemento:
            maximo = elemento
    return maximo

def calcular_maximo_dict(lista: list, campo: str) -> dict:
    """
    Encuentra el diccionario con el valor máximo en un campo específico.

    Args:
    - lista (list): Lista de diccionarios.
    - campo (str): Campo en el que se buscará el valor máximo.

    Returns:
    - dict: Diccionario que contiene el valor máximo en el campo especificado.
    """
    validar_lista(lista)
    maximo = lista[0]  
    for elemento in lista:
        if maximo[campo] < elemento[campo]:
            maximo = elemento
    return maximo

def calcular_minimo_dict(lista: list, campo: str) -> dict:
    """
    Encuentra el diccionario con el valor mínimo en un campo específico.

    Args:
    - lista (list): Lista de diccionarios.
    - campo (str): Campo en el que se buscará el valor mínimo.

    Returns:
    - dict: Diccionario que contiene el valor mínimo en el campo especificado.
    """
    validar_lista(lista)
    minimo = lista[0]  
    for elemento in lista:
        if minimo[campo] > elemento[campo]:
            minimo = elemento
    return minimo

def calcular_minimo(lista: list) -> int:
    """
    Encuentra el valor mínimo en una lista de elementos numéricos.

    Args:
    - lista (list): Lista de elementos numéricos.

    Returns:
    - int: Valor mínimo en la lista.
    """
    validar_lista(lista)
    minimo = lista[0]  
    for elemento in lista:
        if minimo > elemento:
            minimo = elemento
    return minimo

''' FORMALIZAR '''
def formalizar_lista(lista: list):
    """
    Convierte los valores de 'altura', 'peso' y 'fuerza' en cada diccionario de la lista a tipos numéricos específicos.
    
    Args:
    - lista (list): Lista de diccionarios que contiene información sobre elementos con campos 'altura', 'peso' y 'fuerza'.
    
    Returns:
    - None
    """
    for elem in lista:
        elem["altura"] = float(elem["altura"])
        elem["peso"] = float(elem["peso"])
        elem["fuerza"] = int(elem["fuerza"])

''' ORDENAMIENTOS '''
def ordenar_ascendente(lista: list) -> None:
    """
    Ordena una lista de elementos en orden ascendente.

    Args:
    - lista (list): Lista de elementos a ordenar.

    Returns:
    - None
    """
    validar_lista(lista)
    tam = len(lista)
    for i in range(tam-1):
        for j in range(i + 1, tam):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_descendente(lista: list) -> None:
    """
    Ordena una lista de elementos en orden descendente.

    Args:
    - lista (list): Lista de elementos a ordenar.

    Returns:
    - None
    """
    validar_lista(lista)
    tam = len(lista)
    for i in range(tam-1):
        for j in range(i + 1, tam):
            if lista[i] < lista[j]:  
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_lista(lista: list, ascendente: bool = True) -> list:
    """
    Ordena una lista en orden ascendente o descendente.

    Args:
    - lista (list): Lista de elementos a ordenar.
    - ascendente (bool): Indica si se debe ordenar en orden ascendente (True) o descendente (False). Por defecto, es True.

    Returns:
    - list: Lista ordenada.
    """
    validar_lista(lista)
    if ascendente:
        ordenar_ascendente(lista)
    else:
        ordenar_descendente(lista)  
    return lista

def swap_lista(lista:list, i:int, j: int)-> None:
    """
    Intercambia los elementos en las posiciones `i` y `j` de una lista.

    Args:
    - lista (list): Lista en la que se realizará el intercambio.
    - i (int): Índice del primer elemento a intercambiar.
    - j (int): Índice del segundo elemento a intercambiar.

    Returns:
    - None: La función no retorna ningún valor, pero modifica la lista en su lugar.
    """
    auxiliar = lista[i]
    lista[i] = lista [j]
    lista [j] = auxiliar

def ordenar_lista_campo(lista : list, criterio: str, descendente: bool = False):
    """
    Ordena una lista de diccionarios en función de un campo específico.

    Args:
    - lista (list): Lista de diccionarios a ordenar.
    - criterio (str): El campo por el cual se ordenará la lista.
    - descendente (bool): Indicador de si la ordenación debe ser en orden descendente. Por defecto es `False` (ascendente).

    Returns:
    - None: La función no retorna ningún valor, pero ordena la lista en su lugar.
    """
    for i in range (len(lista)-1):
        for j in range (i+1, len(lista)):
            if lista[i][criterio] > lista [j][criterio]:
                swap_lista(lista, i, j)

def ordenar_lista_doble_criterio(lista : list, primer_criterio: str, segundo_criterio:str):
    """
    Ordena una lista de diccionarios utilizando dos criterios de ordenación.

    Args:
    - lista (list): Lista de diccionarios a ordenar.
    - primer_criterio (str): El primer campo por el cual se ordenará la lista.
    - segundo_criterio (str): El segundo campo para desempatar cuando los valores del primer campo son iguales.

    Returns:
    - None: La función no retorna ningún valor, pero ordena la lista en su lugar.
    """
    for i in range (len(lista)-1):
        for j in range (i+1, len(lista)):
            if lista[i][primer_criterio] == lista [j][primer_criterio]:
                if lista[i][segundo_criterio] > lista[j][segundo_criterio]:
                    swap_lista(lista, i, j)
            elif lista[i][primer_criterio] > lista [j][primer_criterio]:
                swap_lista(lista, i, j)

''' BÚSQUEDAS '''
def buscar_dato_dict(lista: list, campo: str, valor) -> dict:
    """
    Busca un diccionario en una lista basado en un campo y un valor específicos.

    Args:
    - lista (list): Lista de diccionarios.
    - campo (str): Nombre del campo en el diccionario.
    - valor: Valor a buscar en el campo especificado.

    Returns:
    - dict or None: Diccionario que cumple con la condición de búsqueda, o None si no se encuentra.
    """
    validar_lista(lista)
    dato = None
    for elem in lista:
        if elem[campo] == valor:
            dato = elem
            break
    return dato

def busqueda_binaria(target, lista: list) -> int:
    """
    Realiza una búsqueda binaria en una lista ordenada para encontrar la posición de un valor específico.

    Args:
    - target: Valor a buscar en la lista.
    - lista (list): Lista de elementos ordenados.

    Returns:
    - int: Índice del valor en la lista, si se encuentra.

    Raises:
    - ValueError: Si el valor no está en la lista.
    """
    validar_lista(lista)
    inferior = 0
    superior = len(lista) - 1
    while inferior <= superior:
        medio = (inferior + superior) // 2
        if lista[medio] == target:
            return medio
        elif target > lista[medio]:
            inferior = medio + 1
        else: 
            superior = medio - 1
    raise ValueError(f"{target} no está en la lista.")

def busqueda_binaria_por_campo(target, campo: str, lista: list) -> int:
    """
    Realiza una búsqueda binaria en una lista de diccionarios ordenada para encontrar la posición de un valor específico en un campo dado.

    Args:
    - target: Valor a buscar en el campo especificado.
    - campo (str): Campo en el que se realizará la búsqueda.
    - lista (list): Lista de diccionarios ordenados por el campo especificado.

    Returns:
    - int: Índice del diccionario en la lista, si se encuentra.

    Raises:
    - ValueError: Si el valor no está en la lista.
    """
    validar_lista(lista)
    inferior = 0
    superior = len(lista) - 1
    while inferior <= superior:
        medio = (inferior + superior) // 2
        if lista[medio][campo] == target:
            return medio
        elif target > lista[medio][campo]:
            inferior = medio + 1
        else: 
            superior = medio - 1
    raise ValueError(f"{target} no está en la lista.")

def buscar_en_lista(lista: list, target) -> bool:
    """
    Busca un valor específico en una lista.

    Args:
    - lista (list): Lista de elementos.
    - target: Valor a buscar en la lista.

    Returns:
    - bool: True si el valor se encuentra en la lista, False en caso contrario.
    """
    for elem in lista:
        if elem == target:
            return True
    return False

def buscar_por_campo(lista: list, campo: str, valor) -> bool:
    """
    Busca un valor específico en un campo dentro de una lista de diccionarios.

    Args:
    - lista (list): Lista de diccionarios.
    - campo (str): Nombre del campo en el diccionario.
    - valor: Valor a buscar en el campo especificado.

    Returns:
    - bool: True si el valor se encuentra en el campo del diccionario, False en caso contrario.
    """
    validar_lista(lista)
    for elem in lista:
        if elem[campo] == valor:
            return True
    return False

''' MAPEO '''
def map_list(funcion, lista: list) -> list:
    """
    Aplica una función a cada elemento de una lista y retorna una nueva lista con los resultados.

    Args:
    - funcion: Función a aplicar a cada elemento de la lista.
    - lista (list): Lista de elementos a los que se aplicará la función.

    Returns:
    - list: Nueva lista con los resultados de aplicar la función a cada elemento.
    """
    lista_retorno = []
    for elem in lista:
        lista_retorno.append(funcion(elem))
    return lista_retorno 

def mapear_campo(lista: list, campo: str) -> list:
    """
    Extrae los valores de un campo específico de cada diccionario en una lista.

    Args:
    - lista (list): Lista de diccionarios.
    - campo (str): Campo del cual se extraerán los valores.

    Returns:
    - list: Lista de valores extraídos del campo especificado.
    """
    validar_lista(lista)
    validar_campo(lista, campo)
    lista_retorno = []
    for elem in lista:
        lista_retorno.append(elem[campo])
    return lista_retorno

''' OS '''
def limpiar_pantalla():
    """
    Limpia la consola.
    """
    system("cls")

def pausa():
    """
    Detiene la ejecución del script y muestra un mensaje que pide al usuario presionar una tecla para continuar.
    """
    system("pause")
