
def readText(ruta):
    with open('./inputs/' + ruta + '.txt', 'r') as file:
        data = file.read().replace('\n', ' ')
        return data