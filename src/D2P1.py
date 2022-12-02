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

def ganador(oponente,yo):
    if oponente == yo:
        return 3
    
    if oponente == 1:
        if yo == 2:
            return 6
        else:
            return 0
    
    if oponente == 2:
        if yo == 1:
            return 0
        else:
            return 6
    
    if oponente == 3:
        if yo == 1:
            return 6
        else:
            return 0
    



total = 0

for dato in datos:
    enfrentamiento = dato.split(' ')
    resultadoEnfrentamiento = ganador(tipo(enfrentamiento[0]),tipo(enfrentamiento[1]))
    miEleccion = tipo(enfrentamiento[1])

    total = total + resultadoEnfrentamiento + miEleccion

print(total)

    
