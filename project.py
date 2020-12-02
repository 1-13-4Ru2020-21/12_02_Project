class objektum:
    def __init__(self, nev, kora):
        self.nev = nev
        self.kora = kora


lista = []
def listafeltoltes(a):
    a.clear()
    a.append(objektum('Juhos Benjamin', 24))
    a.append(objektum('Laboda Dániel', 23))
    a.append(objektum('Hernádi Emma', 20))
    a.append(objektum('Baranyai Áron', 18))
    a.append(objektum('Sánta Ricsi', 19))
    a.append(objektum('Kálmán Gerő', 21))
    a.append(objektum('Ózdi Árpád', 22))


class bub:
    def bubren(self, tomb):
        i = len(tomb)
        for k in range(0, i):
            for j in range(1, i - k):
                if tomb[j - 1].kora > tomb[j].kora:
                    tomb[j], tomb[j - 1] = tomb[j - 1], tomb[j]


class minmax:
    def minimum(self, tomb):
        for i in range(0, len(tomb)):
            mini = i
            for j in range(i + 1, len(tomb)):
                if tomb[j].kora < tomb[mini].kora:
                    mini = j
            tomb[i], tomb[mini] = tomb[mini], tomb[i]

    def maximum(self, szamok):
        max = 0
        for i in szamok:
            if i.kora > max:
                max = i.kora
        print(max)

        for x in range(len(szamok) - 1):
            for j in range(x + 1, len(szamok)):
                if szamok[x].kora > szamok[j].kora:
                    szamok[x], szamok[j] = szamok[j], szamok[x]

    def rendezmaxtombkivel(self, tomb):
        for i in range(0, len(tomb)):
            maxtombi = i
            for j in range(i + 1, len(tomb)):
                if tomb[j].kor > tomb[maxtombi].kor:
                    maxtombi = j
            tomb[i], tomb[maxtombi] = tomb[maxtombi], tomb[i]


def kiir(l):
    for i in l:
        print(i.nev, ' ', i.kora)


listafeltoltes(lista)
print('Eredeti lista:')
kiir(lista)
minmax.minimum(minmax, lista)
print('\nMinimum rendezéses lista:')
kiir(lista)
listafeltoltes(lista)
minmax.maximum(minmax, lista)
print('\nMaximum rendezéses lista:')
kiir(lista)
listafeltoltes(lista)
bub.bubren(bub, lista)
print('\nBuborek rendezéses lista:')
kiir(lista)
