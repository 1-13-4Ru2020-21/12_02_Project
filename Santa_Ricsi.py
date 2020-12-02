def bubren():
    tomb = [50, 2, 16, 1]
    print("Számok")
    print(tomb)
    i = len(tomb)
    for k in range(0, i):
        for j in range(1, i - k):
            if tomb[j - 1] > tomb[j]:
                tomb[j], tomb[j - 1] = tomb[j - 1], tomb[j]
    print("Buborék rendezés")
    print(tomb)
bubren()
