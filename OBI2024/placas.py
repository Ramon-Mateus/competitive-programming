p = input()

nums = ["0","1","2","3","4","5","6","7","8","9"]
hifen = "-"

primeiras_3_a = []
primeiras_3 = False

padBra = []
padMerc = []

resultado = 0

falsa = True

for i in range(0, len(p)):
    if p[i] not in nums and p[i] != hifen:
        if i == 0 or i == 1 or i == 2:
            primeiras_3_a.append(True)
    
    if len(p) == 8:
        if i == 3 and p[i] == hifen:
            padBra.append(True)
        elif i == 4 or i == 5 or i == 6 or i == 7:
            if p[i] in nums:
                padBra.append(True)
    elif len(p) == 7:
        if i == 3 and p[i] in nums:
            padMerc.append(True)
        elif i == 4 and p[i] not in nums and p[i] != hifen:
            padMerc.append(True)
        elif i == 5 or i == 6:
            if p[i] in nums:
                padMerc.append(True)
    else:
        break

if len(primeiras_3_a) == 3:
    primeiras_3 = True

if len(padBra) == 5 and primeiras_3:
    print(1)
elif len(padMerc) == 4 and primeiras_3:
    print(2)
else:
    print(0)