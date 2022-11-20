
def readText(ruta):
    with open('./inputs/' + ruta + '.txt', 'r') as file:
        data = file.read()
        data = data.splitlines()
        return data