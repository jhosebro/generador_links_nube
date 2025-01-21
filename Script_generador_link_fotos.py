import shutil #//* Libreria para copiar el excel
import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
#//*Debemos importar un excel que solo tenga una hoja para evitar que a la hora de hacer la copia no existan conflictos y que las columnas queden en la primera fila


#//* Abrimos ventana de dialogo para seleccionar archivo excel
def seleccionar_y_copiar_excel():
    #//*Creamos la ventana oculta de tkinter
    root = tk.Tk()
    root.withdraw() #//*Ocultamos la ventana
    
    #//*Abrimos la ventana de dialogo para seleccionar un archivo
    ruta_archivo_original = filedialog.askopenfilename(title="Selecciona el archivo excel", filetypes=[("Excel files", "*.xlsx")])
    
    #//*Se verifica si se selecciono un archivo
    if ruta_archivo_original:
        print("Archivo seleccionado: ", ruta_archivo_original)
        copiar_archivo(ruta_archivo_original)
    else:
        print("No se selecciono ningun archivo.")

def copiar_archivo(ruta_archivo_original):
    nombre_archivo = os.path.basename(ruta_archivo_original)
    directorio = os.path.dirname(ruta_archivo_original)
    ruta_archivo_copia = os.path.join(directorio, f"copia_{nombre_archivo}")
    
    try:
        shutil.copy(ruta_archivo_original, ruta_archivo_copia)
        print("Archivo copiado con exito")
        contenido = pd.read_excel(ruta_archivo_copia)
        print(f"Primera fila del archivo copiado: {contenido.columns}")
        return ruta_archivo_copia
    except Exception as e:
        print("Error al copiar el archivo")
        print(e)
        return e
    
#//*Ejecutamos la funcion
seleccionar_y_copiar_excel()

