import os

def menu():
    while True:
        print("\n" + "="*30)
        print(" SISTEMA DE MANTENIMIENTO ")
        print("="*30)
        print("1. Ejecutar Limpiador de Temporales")
        print("2. Ejectuar Respaldo de Archivos")
        print("3. Salir")


        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            print("n\Iniciando Limpiador...")
            os.system("python Limpiador.py")
        elif opcion == "2":
            print("n\Iniciando Respaldo...")
            os.system("python respaldo.py")
        elif opcion == "3":
            print("Saliendo del sistema. ¡Buen trabajo!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()