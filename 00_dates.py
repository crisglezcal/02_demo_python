# ----------------------------------------------------------------------------------------------------
# DATES
# ----------------------------------------------------------------------------------------------------

# DATETIME
    # Agrupa datos de fecha y de tiempo

# Módulo oficial de Python
from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp()

print(timestamp)

year_2023 = datetime(2023, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

# TIME
    # Agrupa los datos de tiempo

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# DATE
    # Agrupa los datos de fechas

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

# TIMEDELTA
    # Operar con diferentes fechas (se puede si son el mismo tipo de objeto)

diff = year_2023 - now
print(diff) # -1173 days, 15:17:45.372632

diff = year_2023.date() - current_date # 56 days, 0:00:00
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
# start_timedelta = 270 días, 0:01:40.000100
    # 10 semanas = 70 días
    # 200 días = 270 días
    # 100 segundos
    # 100 microsegundos
end_timedelta = timedelta(300, 100, 100, weeks = 13)
# end_timedelta = 391 días, 0:01:40.000100
    # 13 semanas = 91 días
    # 300 días = 391 días
    # 100 segundos
    # 100 microsegundos
print(end_timedelta - start_timedelta) # 121 days, 0:00:00
print(end_timedelta + start_timedelta) # 661 days, 0:03:20.000200
