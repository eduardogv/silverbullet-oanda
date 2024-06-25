import pandas as pd
from pytz import timezone

# Genera un rango de fechas y horas localizadas
date_range = pd.to_datetime(pd.date_range('2023-06-01', '2024-06-01', freq='h', tz='America/Denver'))

# Crea un DataFrame con las fechas
df = pd.DataFrame(data=date_range, columns=['date_time'])

# Calcula el ajuste del horario de verano
df['dst_flag'] = df['date_time'].dt.tm_isdst().apply(lambda x: 1 if x.total_seconds() != 0 else 0)

# Ahora df['dst_flag'] contiene 1 para horas en horario de verano y 0 para horas fuera de él


