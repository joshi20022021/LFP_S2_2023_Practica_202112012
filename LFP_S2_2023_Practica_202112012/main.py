def cargar_inventario_inicial():
    print("------------------------------------------------------------------")
    print("Opción 1: Cargar Inventario inicial")
    archivo_inventario = input("Ingrese la ruta del archivo .inv: ")
        
    try:
        with open(archivo_inventario, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            inventario = {}
            
            for linea in lineas:
                instruccion, parametros = linea.strip().split(' ', 1)
                if instruccion == 'crear_producto':
                    try:
                        nombre, cantidad_str, precio_unitario_str, ubicacion = parametros.split(';')
                        cantidad = float(cantidad_str)
                        precio_unitario = float(precio_unitario_str)
                    except ValueError:
                        print(f"Error en el formato de línea: {linea}. Ignorando entrada.")
                        continue
                    
                    if nombre in inventario:
                        if ubicacion == inventario[nombre]['ubicacion']:
                            inventario[nombre]['cantidad'] += cantidad
                            print(f"Se agregaron {cantidad:.2f} unidades de '{nombre}' a '{ubicacion}'.")
                        else:
                            
                            i = 2
                            new_nombre = nombre
                            while new_nombre in inventario:
                                new_nombre = f"{nombre} ({i})"
                                i += 1
                            inventario[new_nombre] = {
                                'cantidad': cantidad,
                                'precio_unitario': precio_unitario,
                                'ubicacion': ubicacion
                            }
                            print(f"Producto '{new_nombre}' agregado al inventario en la ubicación '{ubicacion}'.")
                    else:
                        inventario[nombre] = {
                            'cantidad': cantidad,
                            'precio_unitario': precio_unitario,
                            'ubicacion': ubicacion
                        }
                        print(f"Producto '{nombre}' agregado al inventario en la ubicación '{ubicacion}'.")
                    
            print("------------------------------------------------------------------")
            print("Inventario inicial cargado exitosamente.")
            return inventario
    except FileNotFoundError:
        print("------------------------------------------------------------------")
        print("El archivo no fue encontrado.")
        return {}

def cargar_instrucciones_movimientos(inventario):
    print("------------------------------------------------------------------")
    print("Opción 2: Cargar instrucciones de movimientos")
    archivo_movimientos = input("Ingrese la ruta del archivo .mov: ")
    
    try:
        with open(archivo_movimientos, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            
            for linea in lineas:
                linea = linea.strip()
                if not linea:  
                    continue
                
                instruccion, detalles = linea.split(' ', 1) 
                detalles_partes = detalles.split(';')
                if len(detalles_partes) != 3:
                    print(f"Error en el formato de línea: {linea}. Ignorando entrada.")
                    continue
                
                nombre, cantidad_str, ubicacion = detalles_partes
                try:
                    cantidad = int(cantidad_str)
                except ValueError:
                    print(f"Error en el formato de detalles en línea: {linea}. Ignorando entrada.")
                    continue
                
                if nombre not in inventario:
                    print(f"No se pudo ejecutar la instrucción para {nombre}. Producto no existe en el inventario.")
                    continue
                
                if ubicacion != inventario[nombre]['ubicacion']:
                    print(f"No se pudo ejecutar la instrucción para {nombre}. Ubicación incorrecta.")
                    continue
                
                if instruccion == 'agregar_stock':
                    inventario[nombre]['cantidad'] += cantidad
                    print(f"Se agregaron {cantidad:.2f} unidades de {nombre} a {ubicacion}.")
                elif instruccion == 'vender_producto':
                    if cantidad <= inventario[nombre]['cantidad']:
                        inventario[nombre]['cantidad'] -= cantidad
                        print(f"Se vendieron {cantidad:.2f} unidades de {nombre} de {ubicacion}.")
                    else:
                        print(f"No hay suficiente stock de {nombre} en {ubicacion}.")
                else:
                    print(f"Instrucción no reconocida: {instruccion}")
    except FileNotFoundError:
        print("══════════════════════════════════════════════════════════════════════════════")
        print("El archivo no fue encontrado.")

def crear_informe_inventario(inventario):
    print("Opción 3: Crear informe de inventario")
    nombre_archivo = input("Ingrese el nombre del archivo para el informe (sin extensión): ")
    archivo_salida = f"{nombre_archivo}.txt"

    try:
        with open(archivo_salida, "w", encoding='utf-8') as archivo:
            archivo.write("Informe de Inventario:\n")
            archivo.write("╔═════════════════════════════════════════════════════════════════════════════════╗\n")
            archivo.write("║ Producto   ║   Cantidad   ║   Precio Unitario   ║   Valor Total   ║ Ubicación   ║\n")
            archivo.write("╠═════════════════════════════════════════════════════════════════════════════════╣\n")
            total_valor = 0
            for producto, detalles in inventario.items():
                cantidad = detalles["cantidad"]
                precio_unitario = detalles["precio_unitario"]
                ubicacion = detalles["ubicacion"]
                valor_total = cantidad * precio_unitario
                total_valor += valor_total
                archivo.write(f"║ {producto:<10} ║ {cantidad:>12} ║ {precio_unitario:>20.2f} ║ {valor_total:>15.2f} ║ {ubicacion:<10} ║\n")
            archivo.write("╚═════════════════════════════════════════════════════════════════════════════════╝\n")
            archivo.write(f"Total Valor: {total_valor:>67.2f}\n")      
        print(f"Informe de inventario creado en el archivo '{archivo_salida}'.")
    
    except IOError:
        print("Error al crear el informe de inventario.")

def main():
    inventario = {}
    while True:
        print("╔══════════════════════════════════════════════════════════════════════════════╗")
        print("║              Practica 1 - Lenguajes formales y de programación               ║")
        print("╠══════════════════════════════════════════════════════════════════════════════╣")
        print("║                            Sistema de inventario                             ║")
        print("║                        1. Cargar Inventario inicial                          ║")
        print("║                    2. Cargar instrucciones de movimientos                    ║")
        print("║                       3. Crear informe de inventario                         ║")
        print("║                                  4. Salir                                    ║")
        print("╚══════════════════════════════════════════════════════════════════════════════╝\n")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            inventario = cargar_inventario_inicial()
        elif opcion == '2':
            cargar_instrucciones_movimientos(inventario)
        elif opcion == '3':
            crear_informe_inventario(inventario)
        elif opcion == '4':
            print("══════════════════════════════════════════════════════════════════════════════")
            print("Usted ha salido del programa")
            break
        else:
            print("══════════════════════════════════════════════════════════════════════════════")
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()