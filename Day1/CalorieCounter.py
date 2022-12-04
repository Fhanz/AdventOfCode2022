cal = open("input.txt", "r")
lista = []
num = 0
for line in cal:
    if line != "\n":
        num += int(line[:-1])
    else:
        lista.append(num)
        num = 0
print(sorted(lista, reverse = True)[0]+sorted(lista, reverse = True)[1]+sorted(lista, reverse = True)[2])