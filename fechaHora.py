from datetime import datetime, date, time, timedelta
from funcionFechaChile import formatoFecha

ahora = datetime.now()
#print(ahora)
#print(ahora.utcnow()) # formato UTC
#print(f"{ahora.day}-{ahora.month}-{ahora.year}\{ahora.hour}:{ahora.minute}:{ahora.second}")

#----------------creacion de fecha con parametros-------------------#
hoy = datetime.today()
print(hoy)
formato_date_anio = "%Y-%m-%d"
formato_date_dia = "%d/%m/%Y"
formato_dateTime_anio = "%Y-%m-%d %H:%M:%S"
formato_dateTime_dia = "%d/%m/%Y\%H:%M:%S"
formato_time = "%H:%M:%S"
print(f"fecha con formato date {hoy.strftime(formato_date_anio)}")
print(f"fecha y hora con formato datetime {hoy.strftime(formato_dateTime_anio)}")

#----------convertir una cadena a un objeto datetime-----------------------#

objeto_dateTime = datetime.strptime("2020-08-04",formato_date_anio) # convierte un string en formato fecha, se debe pasar los mismos parametros de orden
print(objeto_dateTime)

#------------------operaciones con fechas (weeks, days, hours, minutes, seconds, milliseconds)-------------------------#

fecha = date.today()
dia_anterior = fecha-timedelta(days=1)
dia_siguiente = fecha+timedelta(days=1)
dos_meses_siguiente = fecha+timedelta(weeks=8)
# print(f"fecha menos un dia formato año: {dia_anterior}")
# print(f"fecha menos un dia formato dia: {dia_anterior.strftime(formato_date_dia)}")
# print(f"fecha mas un dia formato año: {dia_siguiente}")
# print(f"fecha mas un dia formato dia: {dia_siguiente.strftime(formato_date_dia)}")
#print(f"fecha mas dos meses formato año: {dos_meses_siguiente}")
print(f"fecha mas dos meses formato dia: {dos_meses_siguiente.strftime(formato_date_dia)}")

#----------------- diferencias entre dos fechas----------------------#

fecha1 = date.today()
fecha_hora1 = datetime.now()
fecha2 = date(2019, 9, 22 )
fecha_hora2 = datetime(2019, 9, 22, 0, 0, 0)
diferencia_fecha = fecha1-fecha2
diferencia_fechaHora = fecha_hora1-fecha_hora2
#print(f"hay {diferencia_fecha.days} dias de diferencia en fecha")
print(f"hay {diferencia_fechaHora.days} dias de diferencia en fecha hora")

#-------Dia de semana, python los reconoce 0 = lunes, 1 = martes, 2 = miercoles, etc----#

print(f"dia de la semana {datetime.weekday(fecha_hora1)}")

#--------Convertir a timestamp-------------------#

print(f"fecha Hora = {fecha_hora1} | timestamp de fecha hora = {datetime.timestamp(fecha_hora1)} | Convertir de timestamp a datetime = {datetime.fromtimestamp(1600825273.584699)}")

print(formatoFecha("2020-07-26"))
print(f"{formatoFecha(hoy.strftime(formato_date_anio))} con hora {hoy.strftime(formato_time)}")


#editado desde github

