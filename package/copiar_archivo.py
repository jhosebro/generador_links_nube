import shutil # * Libreria para copiar el excel
import os

# * Debemos proporcionar una ruta adecuada para el archivo que se va a copiar
def copiar_archivo(ruta_archivo_original):
    
    #! Copia un archivo Excel desde la ruta proporcionada, lee su contenido y retorna la ruta de la copia.
    
    # * Obtenemos el nombre del archivo desde su ruta original
    nombre_archivo = os.path.basename(ruta_archivo_original)
    # * Obtenemos el directorio donde se encuentra el archivo original
    directorio = os.path.dirname(ruta_archivo_original)
    # * Generamos la ruta para la copia del archivo
    ruta_archivo_copia = os.path.join(directorio, f"copia_{nombre_archivo}")
    
    try:
        #! Intentamos copiar el archivo original a la nueva ubicación
        shutil.copy(ruta_archivo_original, ruta_archivo_copia)
        print("Archivo copiado con exito")
        return ruta_archivo_copia # * Retornamos la ruta del archivo copiado
    except Exception as e:
        #! Capturamos cualquier error que ocurra durante la copia o lectura del archivo
        print(f"Error al copiar el archivo: {e}")
        return None