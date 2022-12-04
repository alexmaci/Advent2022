import reader as r

datos = r.readText('D4')

def p1(rangos):
    bloque1 = rangos[0]
    bloque2 = rangos[1]
    
    rango1 = bloque1.split('-')
    rango2 = bloque2.split('-')

    iniBloque1 = int(rango1[0])
    finBloque1 = int(rango1[1])

    iniBloque2 = int(rango2[0])
    finBloque2 = int(rango2[1])

    if iniBloque1 <= iniBloque2 and finBloque1 >= finBloque2:
        return True
    if iniBloque2 <= iniBloque1 and finBloque2 >= finBloque1:
        return True
    return False


contador = 0       

for dato in datos:
    rangos = dato.split(',') 
    if p1(rangos):
        contador = contador + 1

print(contador)