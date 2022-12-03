import reader as r

datos = r.readText('D3')

indices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def coincidencia(string1, string2):
    for letra1 in string1:
        for letra2 in string2:
            if letra1 == letra2:
                return letra1

total = 0

for dato in datos:
    longitud = len(dato)

    s1 = slice(0,longitud//2)
    s2 = slice(longitud//2,longitud)

    string1=dato[s1]
    string2=dato[s2]

    letra = coincidencia(string1,string2)
    total = total + (indices.index(letra) + 1)

print(total)





    