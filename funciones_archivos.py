import re
import json

#PREGUNTAR CÚAL USAR

def parser_csv_re(path: str)-> list:
    """
    Lee un archivo CSV y devuelve una lista de diccionarios basada en su contenido.

    Args:
    - path (str): Ruta del archivo CSV.

    Returns:
    - list: Lista de diccionarios con la información leída del archivo CSV.
    """
    lista = []
    try :
        with open (path, "r", encoding= "utf8") as archivo:
            campo = re.split (",|\n", archivo.readline())
            for lineas in archivo:
                registro = re.split (",|\n", lineas)
                diccionario = {}
                diccionario = {
                campo[0]: int (registro [0]),
                campo[1]: registro [1],
                campo[2]: registro [2],
                campo[3]: int (registro [3]),
                }
                lista.append (diccionario)
        return lista
    except FileNotFoundError:
        print (f"Error. La ruta '{path}' no existe")

def parser_csv(path: str)-> list: #parser con readline pero sin re
    """
    Lee un archivo CSV y devuelve una lista de diccionarios basada en su contenido.

    Args:
    - path (str): Ruta del archivo CSV.

    Returns:
    - list: Lista de diccionarios con la información leída del archivo CSV.
    """
    lista = []
    try :
        with open (path, "r", encoding= "utf8") as archivo:
            campo = archivo.readline().strip().split(",")
            for lineas in archivo:
                registro = lineas.strip().split(",")
                diccionario = {}
                diccionario = {
                campo[0]: int (registro [0]),
                campo[1]: registro [1],
                campo[2]: registro [2],
                campo[3]: int (registro [3]),
                }
                lista.append (diccionario)
        return lista
    except FileNotFoundError:
        print (f"Error. La ruta '{path}' no existe")

def parser_csv_2(path: str)-> list: #parser sin usar re ni readline
    """Lee un arhivo csv y devuelve una lista de diccionarios del contenido.

    Args:
        path (str): recibe la ruta del archivo.

    Returns:
        list: lista de diccionarios con el contenido del archivo csv
    """
    lista = []
    try :
        with open (path, "r", encoding= "utf8") as archivo:
            contenido = archivo.read().strip().split("\n")
            campo = contenido[0].split(",")
            for lineas in contenido[1:]:
                valor = lineas.split(",")
                diccionario = {}
                diccionario = {
                campo[0]: int (valor [0]),
                campo[1]: valor [1],
                campo[2]: valor [2],
                campo[3]: int (valor [3]),
                }
                lista.append (diccionario)
        return lista
    except FileNotFoundError:
        print (f"Error. La ruta '{path}' no existe")


#--------------------------------------------------------------

def generar_csv(path: str, lista: list):
    """
    Guarda una lista de diccionarios en un archivo CSV.

    Args:
    - path (str): Ruta del archivo CSV.
    - lista (list): Lista de diccionarios a guardar en el archivo CSV. Cada diccionario debe contener las claves 
      'id_bike', 'nombre', 'tipo', y 'tiempo'.

    Returns:
    - None
    """
    with open(path, "w", encoding="utf-8") as archivo:
        for elemento in lista:
            linea = f"{elemento['id_bike']},{elemento['nombre']},{elemento['tipo']},{elemento['tiempo']}\n"
            archivo.write(linea)


#------------------------------


def parser_json(path:str)-> list:
    """
    Lee un archivo JSON y devuelve una lista de diccionarios basada en su contenido.

    Args:
    - path (str): Ruta del archivo JSON.

    Returns:
    - list: Lista de diccionarios con la información leída del archivo JSON.
    """
    with open (path, "r") as archivo:
        diccionario = json.load(archivo)
    
    return diccionario["key"]


def generar_json(path: str, lista:list):
    """
    Guarda una lista de diccionarios en un archivo JSON.

    Args:
    - path (str): Ruta del archivo JSON.
    - lista (list): Lista de diccionarios a guardar en el archivo JSON.

    Returns:
    - None
    """
    with open (path, "w") as archivo:
        json.dump(lista, archivo, indent = 4)

