
import os
import shutil

def limpiar_especifico(ruta_carpeta):
    print(f"--- ANALIZANDO: {ruta_carpeta} ---")

    if not os.path.exists(ruta_carpeta):
        print(f"[!] La ruta no existe: {ruta_carpeta}")
    
    encotrados = 0
    for archivo in os.listdir(ruta_carpeta):
        ruta_completa = os.path.join(ruta_carpeta, archivo)
        try:
            if os.path.isfile(ruta_completa) or os.path.islink(ruta_completa):
                os.remove(ruta_completa)
                print(f"[OK] Archivo borrado: {archivo}")
                encontrados += 1
            elif os.path.isdir(ruta_completa):
                shutil.rmtree(ruta_completa)
                print(f"[OK] Carpeta eliminada {archivo}")
                encontrados += 1
        except Exception as e:
            print(f"[!] No se pudo borrar: {archivo}: {e}")
    print(f"--- LIMPIEZA COMPLETADA: {encontrados} elementos eliminados ---\n")

    carpetas_a_limpiar = [
        os.path.join(os.environ['USERPROFILE'], 'Downloads', 'Temporales_Prueba'),
        os.path.join(os.environ['TEMP'])
    ]
    for c in carpetas_a_limpiar:
        limpiar_especifico(c)