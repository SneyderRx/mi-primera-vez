from logic.formula import hi

def desing():
    print("Bienvenido al mejor sistma del mundo")
    print("     0. Atrás")
    print("     1. ¿Deseas que nuestra máquina salude?")
    opc = int(input("Elija una de nuestras opciones disponibles: "))
    if(opc == 1):
        name = input("Ingrese su nombre: ")
        result = hi(name)
        print(result)
    return opc