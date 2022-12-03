import reader as r

datos = r.readText('D3')
indices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def coincidencia(string1, string2,string3):
    for letra1 in string1:
        for letra2 in string2:
            for letra3 in string3:
                if letra1 == letra2 and letra2 == letra3:
                    return letra1

indice = 0
total = 0

while indice < len(datos):

    item1=datos[indice]
    item2=datos[indice+1]
    item3=datos[indice+2]

    letra = coincidencia(item1,item2,item3)

    total += indices.index(letra) + 1

    indice += 3

print (total)