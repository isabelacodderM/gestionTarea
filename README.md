## Aplicación para gestionar tareas
Permite: agregar tareas, listar tareas, buscar por categoría, mostrar tareas unicas por categorías
y calcular estadísticas de tareas.

- Listas: `tareas` es una lista que almacena todas las tareas.
- Tuplas: cada tarea se guarda como una tupla `(titulo, categoria, prioridad)`.
- Diccionarios: `conteo_por_categoria` almacena la cantidad de tareas por categoría.
- Sets: `categorias` guarda categorías únicas sin repetir.

## Uso de ciclos

- `for`: se usa para iterar la lista de tareas al listar tareas, buscar categorías y mostrar
  categorías únicas.
- `while`: se usa en `mostrar_estadisticas` para recorrer la    lista de tareas con un índice manual
  y también en el menú principal para repetir la ejecución hasta que el usuario elija salir.

## Requisitos

- Python 3.x

## Ejecución

1. Abre una terminal.
2. Navega al directorio del proyecto:

bash:
cd c:\Users\potos\Desktop\tienda_store
3. Ejecuta el programa:

powershell:
python .\main.py

4. Sigue las instrucciones en pantalla para agregar tareas, listar o buscar por categoría.

