import os
try:
    from colorama import Fore, Style, init
except ImportError:
    print("Instalando galeria de colores...")
    os.system('pip install colorama')
    from colorama import Fore, Style, init


#Inicia los colores
init(autoreset=True)


#Configuracion de colores Cyber (Rojo y Purpura)
RED = Fore.RED
PURPLE = Fore.MAGENTA
CYAN = Fore.CYAN
RESET = Style.RESET_ALL


def mostrar_logo():
    print(f"{PURPLE}      SISTEMA DE MANTENIMIENTO ")
    print(f"{RED}===========================================")
    print(f"{RED}    [ PORTAFOLIO TÉCNICO - BENJAMIN ]")
    print(f"{RED}===========================================")
    print(f"{CYAN} 1.{RESET} Ejecutar Limpiador")
    print(f"{CYAN} 2.{RESET} Realizar Respaldo")
    print(f"{CYAN} 3.{RESET} Ver Soporte Tecnico")
    print(f"{RED}-------------------------------------------")
    print(f"{PURPLE} >> Seleccione una opción: ", end="")



    opcion = input()

    if opcion == "1":
        print(f"{CYAN} INICIANDO LIMPIADOR...{RESET}")
        import Limpiador
    elif opcion == "2":
        print(f"{CYAN}Iniciando Respaldo...{RESET}")
        import respaldo
    elif opcion == "3":
        print(f"{CYAN}Abriendo Soporte...{RESET}")
        import soporte
    else:
        print(f"{RED}Opción no Válida.{RESET}")


mostrar_logo()