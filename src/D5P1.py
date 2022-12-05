import reader as r

datos = r.readText('D5')

def loadCrates(datos):
    crates = [[],[],[],[],[],[],[],[],[]]
    stack = datos[:8]
    for i in reversed(range(8)):
        for j in range(1,36,4):
            indice = int((j-1)/4)
            if stack[i][j] != ' ':
                crates[indice].append(stack[i][j])
    
    return crates
 
def mover(datos, crates):
    for dato in datos: 
        array = dato.split(' ')
        numero = int(array[1])
        desde = int(array[3])
        hasta = int(array[5])
        for i in range(numero):
            sacado = crates[desde-1].pop()
            crates[hasta-1].append(sacado)

    return crates

crates = loadCrates(datos)
crates = mover(datos[10:], crates)

for ele in crates:
    print(ele.pop()) 
