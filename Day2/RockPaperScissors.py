strategy = open("input.txt", "r")
lista = []
for element in strategy:
    pair = element[:-1].split(" ")
    lista.append(pair)
#print(lista)
#rock: A, X
#paper: B, Y
#scissors: C, Z
draw = {"A": "X", "B": "Y", "C": "Z"}
#loss = {"A": "Z", "B": "X", "C": "Y"}
win  = {"A": "Y", "B": "Z", "C": "X"}
base = {"X": 1, "Y": 2, "Z": 3}
def score(pair):
    points = base[pair[1]]
    if draw[pair[0]] == pair[1]:
        points += 3
    if win[pair[0]] == pair[1]:
        points += 6
    return points
suma = 0
for element in lista:
    #print((element, score(element)))
    suma += score(element)
print(suma)

draw2 = {"A": "A", "B": "B", "C": "C"}
loss2 = {"A": "C", "B": "A", "C": "B"}
win2   = {"A": "B", "B": "C", "C": "A"}
base2 = {"A": 1, "B": 2, "C": 3}
def score2(pair):
    points = 0
    if pair[1] == "X":
        comp = loss2[pair[0]]
    elif pair[1] == "Y":
        comp = draw2[pair[0]]
        points += 3
    else:
        comp = win2[pair[0]]
        points += 6
    points += base2[comp]
    return points

suma2 = 0
for element in lista:
    #print((element, score(element)))
    suma2 += score2(element)
print(suma2)