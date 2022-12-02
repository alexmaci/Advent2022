import reader as r

datos = r.readText('D2')

def tipo(input):
    if input == 'A' or input == 'X':
        #piedra
        return 1
    if input == 'B' or input == 'Y': 
        #papel
        return 2
    if input == 'C' or input == 'Z': 
        #tijera
        return 3

def tarea(oponente, resultado):
    if resultado == 'Y':
        return tipo(oponente)
    if resultado == 'X':
        if  tipo(oponente)-1 <= 0:
            return 3
        return tipo(oponente)-1
    if resultado == 'Z':
        if tipo(oponente)+1 >= 4:
            return 1
        return tipo(oponente)+1

total = 0

for dato in datos:
    enfrentamiento = dato.split(' ')
    resultado = (tipo(enfrentamiento[1]) - 1) * 3

    enfrentar = tarea(enfrentamiento[0],enfrentamiento[1])
    total = total + resultado + enfrentar

print(total)
