import tkinter as tk
from tkinter import filedialog
def cargar_inventario_inicial():
    print("Opción 1: Cargar Inventario inicial")
    archivo_inventario = filedialog.askopenfilename(title="Seleccionar archivo .inv", filetypes=[("Archivos de Inventario", "*.inv")])
        
    try:
        with open(archivo_inventario, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            inventario = {}
            
            for linea in lineas:
                instruccion, parametros = linea.strip().split(' ', 1)
                if instruccion == 'crear_producto':
                    nombre, cantidad, precio_unitario, ubicacion = parametros.split(';')
                    inventario[nombre] = {
                        'cantidad': int(cantidad),
                        'precio_unitario': float(precio_unitario),
                        'ubicacion': ubicacion
                    }
            
            print("Inventario inicial cargado exitosamente.")
            return inventario
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return {}

def cargar_instrucciones_movimientos(inventario):
    print("Opción 2: Cargar instrucciones de movimientos")
    archivo_movimientos = filedialog.askopenfilename(title="Seleccionar archivo .mov", filetypes=[("Archivos de Movimientos", "*.mov")])
    
    try:
        with open(archivo_movimientos, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            
            for linea in lineas:
                instruccion, parametros = linea.strip().split(' ', 1)
                if instruccion == 'agregar_stock':
                    nombre, cantidad, ubicacion = parametros.split(';')
                    if nombre in inventario and ubicacion == inventario[nombre]['ubicacion']:
                        inventario[nombre]['cantidad'] += int(cantidad)
                        print(f"Se agregaron {cantidad} unidades de {nombre} a {ubicacion}.")
                    else:
                        print(f"No se pudo agregar stock de {nombre} a {ubicacion}.")
                else:
                    print(f"Instrucción no reconocida: {instruccion}")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")

def vender_producto(inventario, nombre, cantidad, ubicacion):
    if nombre in inventario and ubicacion == inventario[nombre]['ubicacion']:
        if inventario[nombre]['cantidad'] >= cantidad:
            inventario[nombre]['cantidad'] -= cantidad
            print(f"Se vendieron {cantidad} unidades de {nombre} de {ubicacion}.")
        else:
            print(f"No hay suficiente stock de {nombre} en {ubicacion}.")
    else:
        print(f"No se pudo vender {nombre} en {ubicacion}.")

def crear_informe_inventario(inventario):
    print("Opción 3: Crear informe de inventario")
    nombre_archivo = input("Ingrese el nombre del archivo para el informe (sin extensión): ")
    archivo_salida = f"{nombre_archivo}.txt"

    try:
        with open(archivo_salida, "w", encoding='utf-8') as archivo:
            archivo.write("Informe de Inventario:\n")
            archivo.write("{:<15} {:<10} {:<15} {:<15} {:<10}\n".format("Producto", "Cantidad", "Precio Unitario", "Valor Total", "Ubicación"))
            archivo.write("-" * 70 + "\n")

            for producto, detalles in inventario.items():
                cantidad = detalles["cantidad"]
                precio_unitario = detalles["precio_unitario"]
                ubicacion = detalles["ubicacion"]
                valor_total = cantidad * precio_unitario

                archivo.write("{:<15} {:<10} ${:<15} ${:<15} {:<10}\n".format(producto, cantidad, precio_unitario, valor_total, ubicacion))
            
            print(f"Informe de inventario creado en el archivo '{archivo_salida}'.")
    except IOError:
        print("Error al crear el informe de inventario.")


def main():
    inventario = {}
    while True:
        print("-" * 48)
        print("Practica 1 - Lenguajes formales y de programación")
        print("-" * 48)
        print("Sistema de inventario:")
        print("1. Cargar Inventario inicial")
        print("2. Cargar instrucciones de movimientos")
        print("3. Crear informe de inventario")
        print("4. Vender producto")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            inventario = cargar_inventario_inicial()
        elif opcion == '2':
            cargar_instrucciones_movimientos(inventario)
        elif opcion == '3':
            crear_informe_inventario(inventario)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            ubicacion = input("Ingrese la ubicación: ")
            vender_producto(inventario, nombre, cantidad, ubicacion)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()