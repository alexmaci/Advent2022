import reader as r

datos = r.readText('D1')
caloriasActuales = 0
caloriasTotales = []

for dato in datos:
    if dato != '':
        caloriasActuales = caloriasActuales + int(dato)
    else:
        caloriasTotales.append(caloriasActuales)
        caloriasActuales = 0

caloriasTotales.sort(reverse=True)
top3 = caloriasTotales[0:3]
acumular = 0
for ele in top3:
    acumular = acumular + ele

print(acumular)