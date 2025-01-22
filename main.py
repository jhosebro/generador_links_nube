from package.copiar_archivo import copiar_archivo
from package.seleccionar_archivo_excel import seleccionar_excel
from package.verificador_creador_columnas import verificar_columnas

#?? Debemos importar un excel que solo tenga una hoja para evitar que a la hora de hacer la copia no existan conflictos y que las columnas queden en la primera fila
#?? Si necesitamos verificar si las columnas existen dentro de un archivo en el siguiente arreglo colocamos las columnas que queremos verificar

columnas_a_verificar = ["FotoLumMod1","FotoLumMod2","FotoLum1DSC","FotoLum1IMG","FotoLum2DSC", "FotoLum2IMG"] # * Columnas que se deben verificar en el archivo Excel

# * Realizamos estas funciones solo una vez para generar una copia del archivo original
#archivo_original = seleccionar_excel()
#archivo = copiar_archivo(archivo_original)

archivo_a_modificar = seleccionar_excel()

# * Si necesitamos verificar las columnas descomentamos la siguiente línea la verificacion demora aproximadamente 70 segundos
verificar_columnas(archivo_a_modificar, columnas_a_verificar)
