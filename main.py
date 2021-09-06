from Cola import Cola
terminar_programa = False
ordenes = Cola()

def menuPrincipal():
    print("***********************************")
    print("|         1.Ingresar Orden        |")
    print("|         2.Entregar Orden        |")
    print("|         3.MostrarOrdenes        |")
    print("|  4.Mostrar datos del estudiante |")
    print("|             5.Salir             |")
    print("***********************************")
    respuesta = input("Ingrese el número de opción que desea realizar\n")

    if int(respuesta) == 1:
        print("Creando nueva orden")
        print("Ingrese el ingrediente a agregarse a la pizza")
        ordenes.agregarOrden(input())
    elif int(respuesta) == 2:
        ordenes.entregarOrden()
    elif int(respuesta) == 3:
        ordenes.desplegarOrdenes()
    elif int(respuesta) == 4:
        print("José Andrés Montenegro Santos")
        print("202004804")
        print("Introducción a la Programación y Computación 2 sección: A")
        print("Ingeniería en Ciencias y Sistemas")
        print("4to Semestre")
    elif int(respuesta) == 5:
        global terminar_programa
        terminar_programa = True

while terminar_programa is not True:
    if __name__== "__main__":
        menuPrincipal()