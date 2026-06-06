# lista de tareas
tareas = []

# contador para los ids
id = 1

# opciones del menu
menu = [
    "1. Agregar tarea",
    "2. Listar tareas",
    "3. Actualizar tarea",
    "4. Eliminar tarea",
    "5. Marcar tarea como completada",
    "6. Salir"
]


def mostrar_menu():
    print("\nGESTOR DE TAREAS")
    print("----------------")

    for opcion in menu:
        print(opcion)


def agregar_tarea():
    global id

    titulo = input("Ingrese el titulo: ")
    descripcion = input("Ingrese la descripcion: ")

    tarea = {
        "id": id,
        "titulo": titulo,
        "descripcion": descripcion,
        "completada": False
    }

    tareas.append(tarea)

    print("Tarea agregada")

    id = id + 1


def listar_tareas():

    if len(tareas) == 0:
        print("No hay tareas")
        return

    print("\nLISTA DE TAREAS")

    for tarea in tareas:

        if tarea["completada"] == True:
            estado = "Completada"
        else:
            estado = "Pendiente"

        print("----------------")
        print("ID:", tarea["id"])
        print("Titulo:", tarea["titulo"])
        print("Descripcion:", tarea["descripcion"])
        print("Estado:", estado)


def actualizar_tarea():

    if len(tareas) == 0:5
    print("No hay tareas")
    return

    dato = input("Ingrese el ID de la tarea: ")

    if dato.isdigit() == False:
        print("Debe ingresar un numero")
        return

    dato = int(dato)

    existe = False

    for tarea in tareas:

        if tarea["id"] == dato:

            nuevo_titulo = input("Nuevo titulo: ")
            nueva_descripcion = input("Nueva descripcion: ")

            tarea["titulo"] = nuevo_titulo
            tarea["descripcion"] = nueva_descripcion

            print("Tarea actualizada")

            existe = True

    if existe == False:
        print("No existe ese ID")


def eliminar_tarea():

    if len(tareas) == 0:
        print("No hay tareas")
        return

    dato = input("Ingrese el ID de la tarea: ")

    if dato.isdigit() == False:
        print("Debe ingresar un numero")
        return

    dato = int(dato)

    existe = False

    for tarea in tareas:

        if tarea["id"] == dato:

            tareas.remove(tarea)

            print("Tarea eliminada")

            existe = True
            break

    if existe == False:
        print("No existe ese ID")


def marcar_completada():

    if len(tareas) == 0:
        print("No hay tareas")
        return

    dato = input("Ingrese el ID de la tarea: ")

    if dato.isdigit() == False:
        print("Debe ingresar un numero")
        return

    dato = int(dato)

    existe = False

    for tarea in tareas:

        if tarea["id"] == dato:

            tarea["completada"] = True

            print("Tarea completada")

            existe = True

    if existe == False:
        print("No existe ese ID")


while True:

    mostrar_menu()

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        agregar_tarea()

    elif opcion == "2":

        listar_tareas()

    elif opcion == "3":

        actualizar_tarea()

    elif opcion == "4":

        eliminar_tarea()

    elif opcion == "5":

        marcar_completada()

    elif opcion == "6":

        print("Fin del programa")
        break

    else:

        print("Opcion incorrecta")