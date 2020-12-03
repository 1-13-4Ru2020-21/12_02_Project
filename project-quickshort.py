class objektum:
    def __init__(self, nev, kora):
        self.nev = nev
        self.kora = kora


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
        maxi = 0
        for i in szamok:
            if i.kora > max:
                maxi = i.kora
        print(maxi)

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


class quick:
    def partition(self, arre, low, high):
        y = (low - 1)
        pivot = arre[high].kora
        for j in range(low, high):
            if arre[j].kora <= pivot:
                y = y + 1
                arre[y], arre[j] = arre[j], arre[y]
        arre[y + 1], arre[high] = arre[high], arre[y + 1]
        ki = y + 1
        return (ki)

    def quicksort(self, arre, low, high):
        if len(arre) == 1:
            return arre
        if low < high:
            pi = quick.partition(self, arre, low, high)
            quick.quicksort(self, arre, low, pi - 1)
            quick.quicksort(self, arre, pi + 1, high)


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


def kiir(li):
    for i in li:
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
listafeltoltes(lista)
n = len(lista)
quick.quicksort(quick, lista, 0, n-1)
print('\nQuick rendezéses lista:')
kiir(lista)
