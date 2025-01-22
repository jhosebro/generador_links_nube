import pandas as pd

# ? Función para verificar si las columnas en las que vamos a colocar los links existen en el archivo Excel
def verificar_columnas(ruta_archivo, columnas_a_verificar):
    """
    #! Verifica si las columnas a verificar existen en el archivo Excel.
    
    :param ruta_archivo: Ruta del archivo Excel a verificar.
    :param columnas_a_verificar: Lista de columnas a verificar.
    :return: Mensaje de éxito al verificar que existen o fueron creadas o error.    
    """
    try:
        print("Verificando columnas...")
        
        # * Cargamos el archivo Excel en un DataFrame
        contenido = pd.read_excel(ruta_archivo)
        
        # * Obtenermos las columnas del archivo
        columnas_actuales = contenido.columns.to_list()
        
        # * Verificamos si las columnas a verificar existen en el archivo
        columnas_faltantes = [col for col in columnas_a_verificar if col not in columnas_actuales]
        
        if columnas_faltantes:
            # * Si faltan columnas, se crean
            for col in columnas_faltantes:
                contenido[col] = ""
            # * Guardamos el archivo con las columnas nuevas
            contenido.to_excel(ruta_archivo, index=False)
            print(f"Se crearon las columnas: {columnas_faltantes}")
        else:
            # * Si todas las columnas existen
            print("Todas las columnas existen")
            return None
        
    except Exception as e:
        # * Capturamos cualquier error que ocurra al leer el archivo
        print(f"Error al leer el archivo: {e}")
        return e
