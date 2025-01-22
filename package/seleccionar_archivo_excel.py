import tkinter as tk
from tkinter import filedialog

# * Función para seleccionar y copiar el archivo Excel
def seleccionar_excel():
    """
    #!Abre una ventana de diálogo para que el usuario seleccione un archivo Excel, lo copia y retorna la ruta del archivo copiado para su posterior procesamiento.
    """
    
    # * Creamos la ventana oculta de tkinter (sin mostrar la ventana principal)
    root = tk.Tk()
    root.withdraw() # *Ocultamos la ventana para que solo aparezca el dialogo
    
    # * Abrimos la ventana de dialogo para seleccionar un archivo
    ruta_archivo_original = filedialog.askopenfilename(title="Selecciona el archivo excel", filetypes=[("Excel files", "*.xlsx")])
    
    # * Se verifica si se selecciono un archivo
    if ruta_archivo_original:
        print("Archivo seleccionado: ", ruta_archivo_original)
        # * retornamos el archivo para ser manejado en el main
        return ruta_archivo_original
    else:
        # * En caso de no seleccionar ningún archivo
        print("No se selecciono ningun archivo.")
        return None # * Retornamos None si no se seleccionó un archivo