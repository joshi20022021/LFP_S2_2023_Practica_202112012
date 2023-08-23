










**MANUAL** 

**TECNICO**


![](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.001.png)


















PROGRAMAS UTILIZADOS

VISUAL STUDIO CODE

![](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.002.png)![File:Visual Studio Code 1.35 icon.svg - Wikimedia Commons](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.003.png)

WINDOWS 10
![](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.004.png)![File:Windows logo - 2012.svg - Wikimedia Commons](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.005.png)





PYTHON

![](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.006.png)![Archivo:Python-logo-notext.svg - Wikipedia, la enciclopedia libre](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.007.png)







Estructuras de lectura

Prueba.inv

![](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.008.png)

prueba.mov

![](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.009.png)

**Función cargar\_Inventario\_Inicial**

Imprime un encabezado y un mensaje para indicar que se está cargando el inventario inicial.

Pide al usuario que ingrese la ruta del archivo .inv que contiene los detalles de los productos.

![ref1]

Abre el archivo en modo de lectura y comienza a leer las líneas del archivo. Para cada línea en el archivo: Divide la línea en dos partes utilizando el primer espacio como separador. La primera parte es la instrucción (por ejemplo, "crear\_producto") y la segunda parte es la cadena de parámetros. Si la instrucción es "crear\_producto", intenta dividir los parámetros en nombre, cantidad, precio unitario y ubicación

![ref2]

Si los valores no se pueden convertir correctamente a números, se maneja la excepción y se ignora la entrada. Comprueba si el nombre del producto ya existe en el inventario. Si existe y la ubicación coincide, agrega la cantidad al producto existente.

![ref3]Si existe pero la ubicación es diferente, agrega el sufijo "(i)" al nombre (donde i es un número incremental) para crear un nuevo nombre y agrega el producto con la nueva clave. Si no existe, agrega el producto al inventario con la clave del nombre y los detalles correspondientes.



![](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.013.png)Imprime mensajes de confirmación y finaliza la función después de procesar todas las líneas del archivo. Si el archivo no se encuentra, maneja la excepción y muestra un mensaje indicando que el archivo no fue encontrado.

**Funcion cargar\_instrucciones\_movimientos**

![ref4]Imprime un encabezado y un mensaje para indicar que se está cargando las instrucciones de movimientos. Pide al usuario que ingrese la ruta del archivo .mov que contiene las instrucciones de movimientos. Abre el archivo en modo de lectura y comienza a leer las líneas del archivo.

Elimina espacios en blanco al principio y al final de la línea. Si la línea está vacía, la ignora y pasa a la siguiente. Divide la línea en dos partes utilizando el primer espacio como separador. La primera parte es la instrucción (por ejemplo, "agregar\_stock" o "vender\_producto"), y la segunda parte son los detalles que contienen el nombre del producto, la cantidad y la ubicación. Divide los detalles en tres partes utilizando el punto y coma como separador. Si no hay exactamente tres partes, muestra un mensaje de error y continúa con la siguiente línea. Intenta convertir la cantidad de productos a un número entero. Si esto falla, muestra un mensaje de error y continúa con la siguiente línea

![ref5]

Verifica si el nombre del producto existe en el inventario. Si no existe, muestra un mensaje de error y continúa con la siguiente línea. Si existe pero la ubicación no coincide, muestra un mensaje de error y continúa con la siguiente línea. Si la instrucción es "agregar\_stock", agrega la cantidad especificada al producto en el inventario. Si la instrucción es "vender\_producto", verifica si hay suficiente cantidad de producto en el inventario para vender. Si hay suficiente, resta la cantidad especificada del producto en el inventario. Si la instrucción no se reconoce, muestra un mensaje de error. Si el archivo no se encuentra, maneja la excepción y muestra un mensaje indicando que el archivo no fue encontrado.

![](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.016.png)



**Funcion crear\_informe\_inventario**

Solicita al usuario que ingrese el nombre del archivo para guardar el informe. Este nombre será usado como parte del nombre del archivo de salida. 

Crea el nombre completo del archivo de salida agregando la extensión .txt al nombre ingresado por el usuario y escribe dentro de el. Posteriormente genera una tabla en el archivo .txt creado. posteriormente recorre cada producto en el inventario buscando en los diccionario el nombre del producto y sus detalles. Calcula el valor total del producto multiplicando la cantidad por el precio unitario. Suma el valor total del producto al valor total acumulado. Escribe una línea en el archivo que contiene los detalles del producto en columnas de la tabla. Cierra el archivo. Si ocurre un error al crear el archivo (por ejemplo, si no se tiene permisos de escritura en la ubicación especificada), muestra un mensaje de error.

![](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.017.png)







**Funcion main**

implementa un menú interactivo y cíclico que permite al usuario gestionar el sistema de inventario. El programa proporciona opciones para cargar productos en el inventario, realizar movimientos de productos (agregar o vender), crear informes detallados del inventario y salir del programa al ingresar a cada una ejecutara la función a la cual está integrada.

![](Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.018.png)


[ref1]: Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.010.png
[ref2]: Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.011.png
[ref3]: Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.012.png
[ref4]: Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.014.png
[ref5]: Aspose.Words.adde0b31-c594-467d-af44-a33747c21056.015.png
