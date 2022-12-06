import reader as r

datos = r.readText('D6')
string = datos[0]
longitud = len(string)

contador = 3
while contador < longitud:

    substring = string[contador-3:contador+1]
    ordenado = sorted(substring)

    if ordenado[0] != ordenado[1] != ordenado[2] != ordenado[3]:
        contador +=1
        print(contador)
        break
    contador += 1
