import reader as r

datos = r.readText('D6')
string = datos[0]
longitud = len(string)

contador = 13
while contador < longitud:

    substring = string[contador-13:contador+1]
    ordenado = sorted(substring)

    if ordenado[0] != ordenado[1] != ordenado[2] != ordenado[3] != ordenado[4] != ordenado[5] != ordenado[6] != ordenado[7] != ordenado[8] != ordenado[9] != ordenado[10] != ordenado[11] != ordenado[12] != ordenado[13]:
        contador +=1
        print(contador)
        break
    contador += 1