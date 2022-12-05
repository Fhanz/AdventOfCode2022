sections = open("input.txt", "r")
lista = []
for line in sections:
    lista.append(line[:-1].split(","))

sec = []
for element in lista:
    sec.append([element[0].split("-"), element[1].split("-")])

print(sec)
#sec[pair][#n(0 or 1)][begin or end]

