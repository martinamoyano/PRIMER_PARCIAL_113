from funciones_archivos import *
from funciones_genericas import *
from funciones_examen import *
from random import randint
from validaciones import *
import os  

menu = (
    '''¡BIENVENIDO AL MENU!
    1. Cargar archivo .CSV
    2. Imprimir lista
    3. Asignar tiempos
    4. Informar ganador
    5. Filtrar por tipo
    6. Informar promedio por tipo
    7. Mostrar posiciones
    8. Guardar posiciones
    9. Salir
    '''
)

# Función principal para iniciar el programa
def iniciar_programa(menu):
    lista_datos = []  # Se inicializa lista_datos como vacía
    seguir = True
    while seguir:
        print(menu)
        opcion = input("Elija una opción (1-9): ")
        os.system("cls")  # Usar os.system para limpiar la consola

        if opcion != "1" and opcion != "9" and len(lista_datos) == 0:
            print("Debe cargar un archivo CSV primero.")
        else:
            match opcion:
                case "1":
                    lista_datos = cargar_archivo()
                    if lista_datos:
                        print("Archivo cargado con éxito.")
                    else:
                        print("No se pudo cargar el archivo o está vacío.")
                case "2":
                    imprimir_lista(lista_datos)
                case "3":
                    lista_datos = map_list(lambda bicicleta: asignar_tiempo(bicicleta), lista_datos)
                case "4":
                    informar_ganador(lista_datos)
                case "5":
                    lista_filtrada = filtrar_por_tipo(lista_datos)
                    if validar_lista(lista_filtrada):
                        primer_elemento = lista_filtrada[0]
                        tipo = primer_elemento['tipo']
                        path = f"{tipo}.csv"
                        generar_csv(path, lista_filtrada)
                    else:
                        print("No se encontraron bicicletas del tipo especificado.")
                case "6":
                    promedios = informar_promedio_tipo(lista_datos)
                    for tipo, promedio in promedios.items():
                        print(f"Tipo: {tipo}, Promedio de tiempo: {promedio:.2f} minutos")
                case "7":
                    mostrar_posiciones(lista_datos)
                case "8":
                    guardar_posiciones(lista_datos)
                case "9":
                    respuesta = input("¿Seguro desea salir? (si/no): ").lower()
                    if respuesta == "si":
                        seguir = False

        if seguir:
            input("Presione Enter para continuar...")
            os.system("cls") 

    print("¡Gracias por utilizar nuestro programa!")


iniciar_programa(menu)
