from api import obtener_datos
from ui import convertir_a_tabla

datos = obtener_datos()

tabla = convertir_a_tabla(datos)

print(tabla)