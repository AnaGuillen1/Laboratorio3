# Sistema de Biblioteca

libros = [
    {"titulo": "Don Quijote", "disponible": True},
    {"titulo": "Cien años de soledad", "disponible": True},
    {"titulo": "El principito", "disponible": True}
]

while True:
    print("\n--- SISTEMA DE BIBLIOTECA ---")
    print("1. Ver libros")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nLista de libros:")
        for i, libro in enumerate(libros):
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"{i+1}. {libro['titulo']} - {estado}")

    elif opcion == "2":
        num = int(input("Ingrese el número del libro a prestar: ")) - 1
        if libros[num]["disponible"]:
            libros[num]["disponible"] = False
            print("Libro prestado con éxito.")
        else:
            print("El libro no está disponible.")

    elif opcion == "3":
        num = int(input("Ingrese el número del libro a devolver: ")) - 1
        if not libros[num]["disponible"]:
            libros[num]["disponible"] = True
            print("Libro devuelto con éxito.")
        else:
            print("Ese libro ya está disponible.")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
