#maximum/minimum kiválasztás pszeudo kóddal
'''
max = t[0]
ciklus i = 1 .. n - 1
    ha t[i]> max akkor
        max = t[i]
    ha vége
ciklus vége
ki max
'''

szamok = [1,21,33,4,50,6,7,8,44,22,45,66]
max = 0
for i in szamok:
    if i > max:
        max=i
print(max)

for x in range(len(szamok)-1):
    for j in range(x+1, len(szamok)):
        if szamok[x]>szamok[j]:
            szamok[x], szamok[j] = szamok[j], szamok[x]
print (szamok[0])

