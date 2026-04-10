print("---SISTEMA DE DIAGNOSTICO TECNICO---")
disco_total = 500 #G
disco_usado = int(input("¿Cuantos GB hay usados en el disco?" ))

espacio_libre = disco_total - disco_usado


if espacio_libre < 50:
    print(f"ALERTA: solo quedan {espacio_libre}GB. ¡Necesitas limpiar el disco!")
else:
     print(f"Todo OK: Tienes {espacio_libre}GB disponibles.")