import reader as r

datos = r.readText('D1')
caloriasActuales = 0
caloriasAlto = 0

for dato in datos:
    if dato != '':
        caloriasActuales = caloriasActuales + int(dato)
    else:
        if caloriasActuales > caloriasAlto:
            caloriasAlto = caloriasActuales
        caloriasActuales = 0

print(caloriasAlto)
