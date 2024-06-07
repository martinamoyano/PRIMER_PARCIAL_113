from funciones_archivos import *
from funciones_genericas import *
from random import randint
from validaciones import *

# Cargar archivo .CSV
def cargar_archivo():
    """
    Carga los datos de un archivo CSV llamado 'bicicletas.csv' y los convierte en una lista de diccionarios.

    Args:
    - None

    Returns:
    - None
    """
    ruta_archivo = "bicicletas.csv"
    lista_datos = parser_csv(ruta_archivo)


# Imprimir lista
def imprimir_lista(lista: list):
    """
    Valida y muestra la lista de diccionarios de bicicletas.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - None
    """
    validar_lista(lista)
    mostrar_lista(lista)


# Asignar tiempos
def asignar_tiempo(bicicleta):
    """
    Asigna un tiempo aleatorio entre 50 y 120 a la bicicleta.

    Args:
    - bicicleta (dict): Diccionario que representa una bicicleta.

    Returns:
    - dict: El diccionario de la bicicleta con el tiempo asignado.
    """
    bicicleta['tiempo'] = randint(50, 120)
    return bicicleta


# Informar ganador
def definir_ganador(lista: list) -> dict:
    """
    Define el ganador de la carrera de bicicletas basándose en el menor tiempo.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - dict: Diccionario con el nombre del ganador y el tiempo si hay un único ganador,
            o una lista de nombres y el tiempo si hay un empate.
    """
    ganador = calcular_minimo_dict(lista, "tiempo")
    tiempo_ganador = ganador["tiempo"]
    
    bicicletas_empatadas = []
    for bicicleta in lista:
        if bicicleta["tiempo"] == tiempo_ganador:
            bicicletas_empatadas.append(bicicleta["nombre"])

    if len(bicicletas_empatadas) == 1:
        return {"Ganador": ganador["nombre"], "Tiempo": tiempo_ganador}
    return {"Empate": bicicletas_empatadas, "Tiempo": tiempo_ganador}


def informar_ganador(lista: list) -> dict:
    """
    Informa el resultado de la carrera, mostrando el ganador o los empatados en tiempo.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - dict: Diccionario con el resultado de la carrera, indicando el ganador o los empatados.
    """
    resultado_carrera = definir_ganador(lista)
    print("------------------------------")
    print("Resultado de la carrera")
    print("------------------------------")
    mostrar_diccionario(resultado_carrera)


# Filtrar por tipo
def filtrar_por_tipo(lista: list) -> list:
    """
    Filtra la lista de bicicletas por el tipo especificado por el usuario.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - list: Lista de diccionarios con bicicletas que corresponden al tipo especificado.
    """
    tipo = input("Ingrese el tipo de bicicleta que desea: ").upper()
    lista_filtrada = filtrar(lista, "tipo", tipo)
    return lista_filtrada

lista_filtrada = filtrar_por_tipo(lista_datos)

if validar_lista(lista_filtrada):
    primer_elemento = lista_filtrada[0]
    tipo = primer_elemento['tipo']
    path = f"{tipo}.csv"
    generar_csv(path, lista_filtrada)
else:
    print("No se encontraron bicicletas del tipo especificado.")


# Informar promedio por tipo
def informar_promedio_tipo(lista: list) -> dict:
    """
    Calcula y muestra el promedio de tiempo por cada tipo de bicicleta en la lista.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - dict: Diccionario con el tipo de bicicleta como clave y su promedio de tiempo como valor.
    """
    tipos = set(mapear_campo(lista, 'tipo'))
    promedios = {}

    for tipo in tipos:
        bicicletas_tipo = filtrar(lista, 'tipo', tipo)
        tiempos = mapear_campo(bicicletas_tipo, 'tiempo')
        if tiempos:
            promedio = calcular_promedio(tiempos)
        else:
            promedio = 0
        promedios[tipo] = promedio

    return promedios


# Mostrar las posiciones
def mostrar_posiciones(lista: list):
    """
    Ordena y muestra la lista de bicicletas según su tiempo de menor a mayor.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - None
    """
    lista_ordenada = ordenar_lista(lista, ascendente=True)
    imprimir_lista(lista_ordenada)


# Guardar posiciones
def guardar_posiciones(lista: list):
    """
    Guarda las posiciones de las bicicletas en un archivo JSON llamado 'posiciones.json'.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - None
    """
    lista_ordenada = ordenar_lista(lista, ascendente=True)
    diccionario = {"bicicletas": lista_ordenada}
    generar_json("posiciones.json", diccionario)
    print("Posiciones guardadas en 'posiciones.json'.")
