import pandas as pd

def generar_enlaces_excel(ruta_excel, columna_ids, columna_nombres, formato_link, salida_excel):
    """
    Esta función genera una nueva columna con enlaces basados en las columnas de IDs y Nombres del archivo Excel.
    
    Parámetros:
    - ruta_excel: str, ruta del archivo Excel de entrada.
    - columna_ids: str, nombre de la columna que contiene los IDs para crear los enlaces.
    - columna_nombres: str, nombre de la columna que contiene los Nombres para crear los enlaces.
    - formato_link: str, formato del enlace. Ejemplo: "https://www.ejemplo.com/item/{ID}/{Nombre}".
    - salida_excel: str, nombre del archivo Excel donde se guardarán los resultados.

    Retorna:
    - Nada, pero guarda el archivo con los enlaces generados.
    """
    # Leer el archivo Excel
    df = pd.read_excel(ruta_excel)
    
    # Generar los enlaces
    df["FotoLum1DSC"] = df.apply(lambda x: formato_link.format(ID=x[columna_ids], Nombre=x[columna_nombres]), axis=1)
    
    # Guardar el archivo con los enlaces
    df.to_excel(salida_excel, index=False)
    print(f"Enlaces generados y guardados en '{salida_excel}'.")
    
    df.to_excel(salida_excel, index=False)
    
    print("Archivo modificado con éxito.")