import shutil # * Libreria para copiar el excel
import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
# * Debemos importar un excel que solo tenga una hoja para evitar que a la hora de hacer la copia no existan conflictos y que las columnas queden en la primera fila


# * Función para seleccionar y copiar el archivo Excel
def seleccionar_y_copiar_excel():
    """
    !Abre una ventana de diálogo para que el usuario seleccione un archivo Excel, lo copia y retorna la ruta del archivo copiado para su posterior procesamiento.
    """
    
    # * Creamos la ventana oculta de tkinter (sin mostrar la ventana principal)
    root = tk.Tk()
    root.withdraw() #//*Ocultamos la ventana para que solo aparezca el dialogo
    
    # * Abrimos la ventana de dialogo para seleccionar un archivo
    ruta_archivo_original = filedialog.askopenfilename(title="Selecciona el archivo excel", filetypes=[("Excel files", "*.xlsx")])
    
    # * Se verifica si se selecciono un archivo
    if ruta_archivo_original:
        print("Archivo seleccionado: ", ruta_archivo_original)
        
        # * Copiar el archivo seleccionado
        excel_a_trabajar = copiar_archivo(ruta_archivo_original)
        
        # * Retornar la ruta del archivo copiado para su posterior procesamiento
        return excel_a_trabajar
    else:
        # * En caso de no seleccionar ningún archivo
        print("No se selecciono ningun archivo.")
        return None # * Retornamos None si no se seleccionó un archivo

def copiar_archivo(ruta_archivo_original):
    """
    !Copia un archivo Excel desde la ruta proporcionada, lee su contenido y retorna la ruta de la copia.
    """
    #* Obtenemos el nombre del archivo desde su ruta original
    nombre_archivo = os.path.basename(ruta_archivo_original)
    #* Obtenemos el directorio donde se encuentra el archivo original
    directorio = os.path.dirname(ruta_archivo_original)
    #* Generamos la ruta para la copia del archivo
    ruta_archivo_copia = os.path.join(directorio, f"copia_{nombre_archivo}")
    
    try:
        #! Intentamos copiar el archivo original a la nueva ubicación
        shutil.copy(ruta_archivo_original, ruta_archivo_copia)
        print("Archivo copiado con exito")
        
        #* Leemos el contenido del archivo copiado
        contenido = pd.read_excel(ruta_archivo_copia)
        
        print(f"Primera fila del archivo copiado: {contenido.columns}") #? Imprime los nombres de las columnas
        
        return ruta_archivo_copia #* Retornamos la ruta del archivo copiado
    except Exception as e:
        #! Capturamos cualquier error que ocurra durante la copia o lectura del archivo
        print(f"Error al copiar el archivo: {e}")
        return None
    
#//*Ejecutamos la funcion
archivo = seleccionar_y_copiar_excel()

