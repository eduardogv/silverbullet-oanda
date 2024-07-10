

#Funcion para obtener hora actual de NY en formato Z UTC-0
import pytz
from datetime import datetime

def obtener_hora_nueva_york_rfc3339():
    # Definir la zona horaria de Nueva York
    zona_horaria_ny = pytz.timezone('America/New_York')

    # Obtener la fecha y hora actual en la zona horaria de Nueva York
    ahora_ny = datetime.now(zona_horaria_ny)

    # Formatear la fecha y hora en el formato deseado
    hora_formateada = ahora_ny.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    return hora_formateada

# Ejemplo de uso
#hora_actual_ny = obtener_hora_nueva_york_rfc3339()
#print("Hora actual en Nueva York:", hora_actual_ny)




# Validacion de horario de verano en NY (retorno booleano)
import pytz
from datetime import datetime

def esta_en_horario_verano_nueva_york():
    # Definir la zona horaria de Nueva York
    zona_horaria_ny = pytz.timezone('America/New_York')

    # Obtener la fecha y hora actual en la zona horaria de Nueva York
    ahora_ny = datetime.now(zona_horaria_ny)

    # Verificar si estamos en horario de verano
    esta_en_horario_verano = ahora_ny.dst() != zona_horaria_ny.dst(None)

    return esta_en_horario_verano

# Ejemplo de uso
#esta_en_horario_verano_nueva_york()


# Hora 04:00 del dia de HOY

import pytz
from datetime import datetime, timedelta

def obtener_hora_04_00_utc_rfc3339():
    # Obtener la fecha y hora actual en UTC+0
    ahora_utc = datetime.now(pytz.utc)

    # Crear un nuevo objeto datetime con la hora fijada a las 04:00 del mismo día
    hora_04_00 = ahora_utc.replace(hour=4, minute=0, second=0, microsecond=0)

    # Formatear la nueva fecha y hora en formato RFC3339 con la 'Z'
    hora_rfc3339 = hora_04_00.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    return hora_rfc3339

# Ejemplo de uso
#hora_04_00_utc_rfc3339 = obtener_hora_04_00_utc_rfc3339()
#print("Hora 04:00 UTC+0 (RFC3339):", hora_04_00_utc_rfc3339)


