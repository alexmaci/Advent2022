import reader as r

datos = r.readText('2021')
stringList = datos.split(' ')
list =  list(map(int, stringList))
length = len(list)-1
times = 0

for i in range(length):
    if list[i] < list[i+1]:
        times = times + 1


print(times)
    