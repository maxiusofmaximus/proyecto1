# Crea un programa que pida un número al usuario un número
# de mes (por ejemplo el 4) y diga cuántos días tiene
# (por ejemplo 30) y el nombre del mes.
# Debes usar una lista.
# Para simplificarlo vamos a suponer que febrero tiene 28 días.
lista_de_meses = ["Enenero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
lista_dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mes_de_usuario = int(input("Ingrese un número del mes del año: ")) - 1
print(f"El mes legido es {lista_de_meses[mes_de_usuario]} y tiene {lista_dias_del_mes[mes_de_usuario]} días")