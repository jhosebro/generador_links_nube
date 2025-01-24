import pandas as pd
import re

def modificar_valores_por_formato(dataframe, columna_origen, columna_destino1, columna_destino2):
    """
    Modifica los valores de una columna según el formato identificado y coloca el valor modificado en una nueva columna.
    
    :param dataframe: DataFrame de pandas que contiene los datos.
    :param columna_origen: Nombre de la columna de la cual se van a extraer los valores.
    :param columna_destino: Nombre de la columna donde se colocarán los valores modificados.
    :return: DataFrame con la nueva columna agregada.
    """
    # * Verficamos si las columnas existen en el dataframe
    if columna_origen not in dataframe.columns:
        raise ValueError(f"La columna {columna_origen} no existe en el DataFrame.")
    if columna_destino1 not in dataframe.columns:
        raise ValueError(f"La columna {columna_destino1} no existe en el DataFrame.")
    if columna_destino2 not in dataframe.columns:
        raise ValueError(f"La columna {columna_destino2} no existe en el DataFrame.")
    
    # * Asegurarnos de que la columna destino tenga el tipo de datos compatible (object)
    dataframe[columna_destino1] = dataframe[columna_destino1].astype("object")
    dataframe[columna_destino2] = dataframe[columna_destino1].astype("object")
    
    # * Quitamos los espacios en blanco
    dataframe[columna_origen] = dataframe[columna_origen].str.replace(r"\s+", "", regex=True)


    # * Iteracion sobre los valores de la columna origen
    for i, valor in enumerate(dataframe[columna_origen]):
        if pd.isna(valor): # Si el valor es NaN lo colocamos como 'Formato sin clasificar'
            dataframe.at[i, columna_destino1] = "No tenemos foto para clasificar"
            dataframe.at[i, columna_destino2] = "No tenemos foto para clasificar"
            continue
        
        valor_str = str(valor) # Convertimos el valor a string
        
        if valor_str == "P": # * Si el valor es 'P'
            dataframe.at[i, columna_destino1] = "No tenemos foto para clasificar"
            dataframe.at[i, columna_destino2] = "No tenemos foto para clasificar"
        
        elif valor_str == "VEROBSERVACIONES": # * Si el valor es 'VER OBSERVACIONES'
            dataframe.at[i, columna_destino1] = "No tenemos foto para clasificar"
            dataframe.at[i, columna_destino2] = "No tenemos foto para clasificar"
        
        elif re.match(r"^\d{1}$", valor_str): # * Si el valor es un número de 1 cifra
            dataframe.at[i, columna_destino1] = f"DSC0000{valor_str}"
            dataframe.at[i, columna_destino2] = f"Solo existe una fotografia"
        
        elif re.match(r"^\d{2}$", valor_str): # * Si el valor es un número de 2 cifras
            dataframe.at[i, columna_destino1] = f"DSC000{valor_str}"
            dataframe.at[i, columna_destino2] = f"Solo existe una fotografia"
            
        elif re.match(r"^\d{3}$", valor_str): # * Si el valor es un número de 3 cifras
            dataframe.at[i, columna_destino1] = f"DSC00{valor_str}"
            dataframe.at[i, columna_destino2] = f"Solo existe una fotografia"
            
        elif re.match(r"^\d{4}$", valor_str): # * Si el valor es un número de 4 cifras
            dataframe.at[i, columna_destino1] = f"DSC0{valor_str}"
            dataframe.at[i, columna_destino2] = f"Solo existe una fotografia"
        
        elif re.match(r"^\d{5}$", valor_str): # * Si el valor es un número de 5 cifras
            dataframe.at[i, columna_destino1] = f"DSC0{valor_str[1:]}"
            dataframe.at[i, columna_destino2] = f"Solo existe una fotografia"
        
        elif re.match(r"^\d{4}-$", valor_str): # * Si el valor es un número de 4 cifras seguido de un guion
            dataframe.at[i, columna_destino1] = f"DSC0{valor_str[:-1]}"
            dataframe.at[i, columna_destino2] = "Solo existe una fotografia"
        
        elif re.match(r"^\d{8}$", valor_str): # * Si el valor es un número de 5 cifras
            primer_numero = valor_str[:4]
            segundo_numero = valor_str[4:]
            dataframe.at[i, columna_destino1] = f"DSC0{primer_numero}"
            dataframe.at[i, columna_destino2] = f"DSC0{segundo_numero}"
            
        elif re.match(r"^\d+(-\d+)+$", valor_str):
            numeros = valor_str.split("-")
            primer_numero = numeros[0]
            segundo_numero = numeros[-1]
            if len(primer_numero) == 3:
                dataframe.at[i, columna_destino1] = f"DSC00{primer_numero}"
            if len(primer_numero) == 4:
                dataframe.at[i, columna_destino1] = f"DSC0{primer_numero}"
            if len(segundo_numero) == 3:
                dataframe.at[i, columna_destino2] = f"DSC00{segundo_numero}"
            if len(segundo_numero) == 4:
                dataframe.at[i, columna_destino2] = f"DSC0{segundo_numero}"
            
        elif re.match(r"^\d{4}(-\d{4})+$", valor_str): # * Si el valor es un rango de números de 4 cifras separados por guiones
            rango = valor_str.split("-")
            dataframe.at[i, columna_destino1] = f"DSC0{rango[0]}"
            dataframe.at[i, columna_destino2] = f"DSC0{rango[-1]}"
            
        elif re.match(r"^\d+\.\d+$", valor_str): # * Si el valor es un numero decimal
            parte_entera = valor_str.split(".")[0]
            if len(parte_entera) == 3:
                dataframe.at[i, columna_destino1] = f"DSC00{parte_entera}"
                dataframe.at[i, columna_destino2] = f"Solo existe una fotografia"
            if len(parte_entera) == 4:
                dataframe.at[i, columna_destino1] = f"DSC0{parte_entera}"
                dataframe.at[i, columna_destino2] = f"Solo existe una fotografia"
        
        elif re.match(r"^\d+(-\d+(\.\d+)?)+$", valor_str): # * Si el valor es un rango de números separados por guiones y contine decimales
            numeros = valor_str.split("-")
            primer_numero = numeros[0]
            segundo_numero = numeros[-1].split(".")[0]
            dataframe.at[i, columna_destino1] = f"DSC0{primer_numero}"
            dataframe.at[i, columna_destino2] = f"DSC0{segundo_numero}"
        
        elif re.match(r"^\d+(-\d+)+-$", valor_str): # * Si el valor es un rango de números separados por guiones y termina en guion
            numeros = valor_str.strip("-").split("-")
            primer_numero = numeros[0]
            segundo_numero = numeros[-1]
            if len(primer_numero) == 3:
                dataframe.at[i, columna_destino1] = f"DSC00{primer_numero}"
            if len(primer_numero) == 4:
                dataframe.at[i, columna_destino1] = f"DSC0{primer_numero}"
            if len(segundo_numero) == 3:
                dataframe.at[i, columna_destino2] = f"DSC00{segundo_numero}"
            if len(segundo_numero) == 4:
                dataframe.at[i, columna_destino2] = f"DSC0{segundo_numero}"
        
        elif re.match(r"^\d+(,\d+)+$", valor_str): # * Si el valor es una lista de números separados por comas
            numeros = valor_str.split(",")
            if len(primer_numero) == 3:
                dataframe.at[i, columna_destino1] = f"DSC00{primer_numero}"
            if len(primer_numero) == 4:
                dataframe.at[i, columna_destino1] = f"DSC0{primer_numero}"
            if len(segundo_numero) == 3:
                dataframe.at[i, columna_destino2] = f"DSC00{segundo_numero}"
            if len(segundo_numero) == 4:
                dataframe.at[i, columna_destino2] = f"DSC0{segundo_numero}"
        
        elif re.match(r"^DSCN\d+$", valor_str): # * Si el valor es un string que empieza con 'DSCN' seguido de un número
            numero = valor_str[4:] # ? Extraemos el número
            if len(numero) == 3:
                dataframe.at[i, columna_destino1] = f"DSC00{numero}"
                dataframe.at[i, columna_destino2] = f"Solo existe una fotografia"
            if len(numero) == 4:
                dataframe.at[i, columna_destino1] = f"DSC0{numero}"
                dataframe.at[i, columna_destino2] = f"Solo existe una fotografia"
        
        elif re.match(r"^\d{4},DSCN\d+$", valor_str): # * Si el valor es un string que empieza con un número de 4 cifras, seguido de una coma y 'DSCN' seguido de un número
            numero = valor_str.split(",")
            numero1 = numero[0]
            numero2 = numero[1][4:]
            dataframe.at[i, columna_destino1] = f"DSC0{numero1}"
            dataframe.at[i, columna_destino2] = f"DSC0{numero2}"
            
        elif re.match(r"^\d+_\d+$", valor_str): # * Si el valor es un string que contiene un número seguido de un guion bajo y otro número
            numeros = valor_str.split("_")
            if len(numeros[0]) == 3:
                dataframe.at[i, columna_destino1] = f"DSC00{numeros[0]}"
            if len(numeros[0]) == 4:
                dataframe.at[i, columna_destino1] = f"DSC0{numeros[0]}"
            if len(numeros[1]) == 3:
                dataframe.at[i, columna_destino2] = f"DSC00{numeros[1]}"
            if len(numeros[1]) == 4:
                dataframe.at[i, columna_destino2] = f"DSC0{numeros[1]}"
        
        elif re.match(r"^DSC\d+,\d+-\d+$", valor_str):  # Formato: DSC00586,1380-1382
            partes = valor_str.split(",")
            dsc_parte = partes[0]
            rango_parte = partes[1].split("-")
            primer_numero = rango_parte[0]
            segundo_numero = rango_parte[1]
            dataframe.at[i, columna_destino1] = dsc_parte
            dataframe.at[i, columna_destino2] = f"DSC0{segundo_numero}"
            
        elif re.match(r"^DSC\d+,\d+$", valor_str): # * Si el valor es un string que empieza con 'DSC' seguido de un número, una coma y otro número
            partes = valor_str.split(",")
            dsc_parte = partes[0]
            numero = partes[1]
            dataframe.at[i, columna_destino1] = dsc_parte
            dataframe.at[i, columna_destino2] = f"DSC0{numero}"
            
        elif valor_str == "s/f": # * Si el valor es 's/f'
            dataframe.at[i, columna_destino1] = "No tenemos foto para clasificar"
            dataframe.at[i, columna_destino2] = "No tenemos foto para clasificar"
            
        elif re.match(r"^DSCN\d+$", valor_str): # * Si el valor es un string que empieza con 'DSCN' seguido de un número
            numero = valor_str[4:]
            if len(numero) == 3:
                dataframe.at[i, columna_destino1] = f"DSC00{numero}"
                dataframe.at[i, columna_destino2] = f"Solo existe una fotografia"
            if len(numero) == 4:
                dataframe.at[i, columna_destino1] = f"DSC0{numero}"
                dataframe.at[i, columna_destino2] = f"Solo existe una fotografia"
        
        elif re.match(r"^\d+-+IMG_\d+$", valor_str): # * Si el valor es un string que empieza con un número seguido de un guion y 'IMG_' seguido de un número
            partes = valor_str.split("-")
            numero = partes[0]
            img_parte = partes[1:]
            if len(numero) == 3:
                dataframe.at[i, columna_destino1] = f"DSC00{numero}"
                dataframe.at[i, columna_destino2] = "La foto es del Formato IMG"
            if len(numero) == 4:
                dataframe.at[i, columna_destino1] = f"DSC0{numero}"
                dataframe.at[i, columna_destino2] = "La foto es del Formato IMG"
            if len(numero) == 5:
                dataframe.at[i, columna_destino1] = f"DSC{numero}"
                dataframe.at[i, columna_destino2] = "La foto es del Formato IMG"
            
        elif re.match(r"^\d\.\d+E\+\d+$", valor_str):
            dataframe.at[i, columna_destino1] = "No tenemos foto para clasificar"
            dataframe.at[i, columna_destino2] = "No tenemos foto para clasificar"
            
        else:
            dataframe.at[i, columna_destino1] = "Formato sin clasificar"
            dataframe.at[i, columna_destino2] = "Formato sin clasificar"
    
    return dataframe