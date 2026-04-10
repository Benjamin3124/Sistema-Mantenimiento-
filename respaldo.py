import os
import shutil
from datetime import datetime


origen = "documentos_importantes"
hoy = datetime.now().strftime("%Y-%m-%d")
destino = f"Backup_{hoy}"

if not os.path.exists(origen):
    os.makedirs(origen)
    with open(f"{origen}/nota_tecnica.txt", "w") as f:
        f.write("Este es un archivo de pruba para el respaldo.")
        print(f"He creado la carpeta '{origen}' con este archivo de prueba.")

if not os.path.exists(destino):
    os.makedirs(destino)
    print(f"Carpeta de respaldo '{destino}' creada.")

archivos = os.listdir(origen)
for nombre_archivo in archivos:
    ruta_completa = os.path.join(origen, nombre_archivo)
    if os.path.isfile(ruta_completa):
        shutil.copy(ruta_completa, destino) 
        print(f"Copiado; {nombre_archivo} -> {destino}") 
print("\n---  ¡RESPALDO FINALIZADO CON EXITO! ---")            