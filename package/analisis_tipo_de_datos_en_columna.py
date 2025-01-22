import pandas as pd
import re

def analizar_tipos_en_columna(dataframe, columna):
    """
    Analiza una columna para determinar los tipos de valores según sus longitudes, patrones
    y tipos específicos para números.
    
    :param dataframe: DataFrame de pandas que contiene los datos.
    :param columna: Nombre de la columna a analizar.
    :return: Un diccionario con las longitudes, patrones y tipos detectados.
    """
    if columna not in dataframe.columns:
        raise ValueError(f"La columna {columna} no existe en el DataFrame.")
    
    resultados = {}
    valores_no_identificados = [] #* Almaceno los valores clasificados como "Otro"
    
    for valor in dataframe[columna]: #* Incluyo los valores nulos
        if pd.isna(valor):
            tipo = "Celda sin contenido"
            longitud = 0
            clave = (longitud, tipo)
            ejemplo = None
        else:
            valor_str = str(valor) #* Convierto el valor a string para un analisis uniforme
            longitud = len(valor_str)
            
            #* Analizamos los patrones mas comunes a encontrar
            if valor_str == "s/f": #?Detectamos las luminarias sin fotos
                tipo = "Sin fotos (s/f)"
            elif valor_str == "VER OBSERVACIONES": #? Detectamos los que es necesario mirar las observaciones para saber porque no hay fotos
                tipo = "Ver observaciones"
            elif re.match(r"^\d+\.\d+$", valor_str): #? Detectamos los que son decimales
                tipo = "Numero decimal"
            elif re.match(r"^\d+$", valor_str): #? Solo numeros
                tipo = f"Solo números {longitud} cifras"
            elif re.match(r"^[a-zA-Z]+$", valor_str): #? Solo letras
                tipo = f"Solo letras"
            elif re.match(r"^[a-zA-Z0-9_]+$", valor_str): #? Alfanumerico
                tipo = f"Alfanumérico"
            elif re.match(r"^\d{3} - \d{4}$", valor_str):  #? Rango numerico "000 - 0000"
                tipo = "Rango numérico (formato '000 - 0000')"
            elif re.match(r"^\d{4} - \d{4}$", valor_str): #? Rango numerico "0000 - 0000"
                tipo = f"Rango numérico (formato '0000 - 0000')"
            elif re.match(r"^\d{4}(,\d{4})+$", valor_str):  #? Valores separados por comas como "0000,0000"
                tipo = "Números separados por comas (formato '0000,0000')"
            elif re.match(r"^[a-zA-Z0-9\-]+$", valor_str): #? Alfanumerico con guiones
                tipo = f"Alfanumerico con guiones"
            elif re.match(r"^\d{4}-\d{4}(\.\d+)?(-\d{4}(\.\d+)?)?$", valor_str):  #? Rango numerico '0000-0000.0-0000.0'
                tipo = "Rango numérico con decimales (formato '0000-0000.0-0000.0')"
            elif re.match(r"^[+-]?\d+(\.\d+)?[eE][+-]?\d+$", valor_str):  #? Notación científica
                tipo = "Notación científica"
            elif re.match(r"^\d+\s\d+$", valor_str):  #? Formato con números separados por un espacio, como '0000 0000'
                tipo = "Números separados por espacio"
            elif re.match(r"^\d+-[a-zA-Z0-9_]+$", valor_str):  #? Formato '00000-IMG_00000'
                tipo = "Número seguido de cadena alfanumérica con guion"
            elif re.match(r"^\d+-\d+-\d+$", valor_str):  #? Formato '0000-0000- 000'
                tipo = "Número seguido de guiones y números con espacio"
            elif re.match(r"^\d+, [a-zA-Z0-9_]+$", valor_str):  #? Formato '0000, DSCN000'
                tipo = "Número seguido de coma y cadena alfanumérica"
            elif re.match(r"^[a-zA-Z0-9_]+, \d+-\d+$", valor_str):  #? Formato 'DSC00000, 0000-0000'
                tipo = "Cadena alfanumérica seguida de números con guion"
            elif re.match(r"^\d+- \d+$", valor_str):  #? Formato '000- 0000'
                tipo = "Número seguido de guion y otro número con espacio"
            elif re.match(r"^[a-zA-Z0-9_]+, \d+$", valor_str):  #? Formato 'DSC00000, 0000'
                tipo = "Cadena alfanumérica seguida de coma y número"
            elif re.match(r"^\d+-\d+-\s?\d+$", valor_str):  #? Formato '0000-0000- 000'
                tipo = "Número seguido de guiones y números con espacio"
            else:
                tipo = "Tipo no identificado"
                valores_no_identificados.append(valor)
                #? Imprimo el valor que no se pudo identificar
                continue #* Saltamos porque agregamos estos valores al dicccionario de principal
            ejemplo = valor_str   
            clave = (longitud, tipo)
            
        #! Guardamos los resultados
        if clave not in resultados:
            resultados[clave] = {"cantidad": 0, "ejemplo": ejemplo}
        resultados[clave]["cantidad"] += 1 #* Sumamos 1 al valor de la clave adicionando cantidad de valores por tipo
            
        #* Imprimimos valores no identificados
    if valores_no_identificados:
        print("Valores no identificados:")
        for valor in valores_no_identificados:
            print(f" - {valor}")
    else:
        print("Todos los valores fueron identificados")
    
    return resultados

            
            