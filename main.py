def mostrar_menu():
    print("\n--- GESTIÓN DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Buscar tareas por categoría")
    print("4. Mostrar tareas únicas por categoría")
    print("5. Salir")


def agregar_tarea(tareas):
    titulo = input("Título de la tarea: ").strip()
    categoria = input("Categoría (estudio/trabajo/hogar): ").strip().lower()
    prioridad = input("Prioridad (alta/media/baja): ").strip().lower()

    tarea = (titulo, categoria, prioridad)
    tareas.append(tarea)
    print(f"Tarea agregada: {tarea}")


def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
        return

    print("\nLista de tareas:")
    for indice, tarea in enumerate(tareas, start=1):
        titulo, categoria, prioridad = tarea
        print(f"{indice}. {titulo} | Categoría: {categoria} | Prioridad: {prioridad}")


def buscar_por_categoria(tareas):
    categoria_buscar = input("Ingrese la categoría a buscar: ").strip().lower()
    tareas_encontradas = []

    for tarea in tareas:
        titulo, categoria, prioridad = tarea
        if categoria == categoria_buscar:
            tareas_encontradas.append(tarea)

    if tareas_encontradas:
        print(f"\nTareas en la categoría '{categoria_buscar}':")
        for tarea in tareas_encontradas:
            titulo, categoria, prioridad = tarea
            print(f"- {titulo} | Prioridad: {prioridad}")
    else:
        print(f"No se encontraron tareas en la categoría '{categoria_buscar}'.")


def mostrar_categorias_unicas(tareas):
    categorias = set()

    for tarea in tareas:
        categorias.add(tarea[1])

    print("\nCategorías únicas encontradas:")
    for categoria in categorias:
        print(f"- {categoria}")


def mostrar_estadisticas(tareas):
    if not tareas:
        print("No hay tareas para calcular estadísticas.")
        return

    conteo_por_categoria = {}
    indice = 0

    while indice < len(tareas):
        titulo, categoria, prioridad = tareas[indice]
        conteo_por_categoria[categoria] = conteo_por_categoria.get(categoria, 0) + 1
        indice += 1

    print("\nCantidad de tareas por categoría:")
    for categoria, cantidad in conteo_por_categoria.items():
        print(f"- {categoria}: {cantidad}")


def main():
    tareas = []  
    print("Bienvenido al gestor de tareas.")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
            mostrar_estadisticas(tareas)
        elif opcion == "3":
            buscar_por_categoria(tareas)
        elif opcion == "4":
            mostrar_categorias_unicas(tareas)
        elif opcion == "5":
            print("Saliendo. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
