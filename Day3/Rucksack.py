mochilas = open("input.txt", "r")

lista = []
for element in mochilas:
    mochila = element[:-1].split(" ")
    lista.append(mochila)


def compare(backpack):
    match = ""
    size = len(backpack)
    first = backpack[: size // 2]
    second = backpack[size // 2 :]
    for item_first in first:
        for item_second in second:
            if item_first == item_second:
                match = item_first
    return match


def score(letter):
    scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(scores)):
        if letter == scores[i]:
            pt = i + 1
    return pt


total_score = 0

# for element in lista:
#    for text in element:
# print(compare(text))
# print(score(compare(text)))
#        total_score += score(compare(text))

# print(total_score)


def common(bp1, bp2, bp3):
    match = ""
    for let1 in bp1:
        for let2 in bp2:
            for let3 in bp3:
                if let1 == let2 and let1 == let3:
                    match = let1
    return match


for i in range(0, len(lista), 3):
    letra = common(lista[i][0], lista[i + 1][0], lista[i + 2][0])
    total_score += score(letra)

print(total_score)
