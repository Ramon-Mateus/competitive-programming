k = int(input())

for x in range(k):
    n = int(input())
    divs = []
    num = 0
    soma = 0
    div = 0

    for w in range(n - 1, 1, -1):
        if n % w == 0:
            divs.append(w)
    
    divs.sort(reverse=True)
    
    for z in range(n - 1 , 1, -1):
        for l in range(len(divs)):
            #print(z, "%", divs[l])
            if z % divs[l] == 0 and divs[l] + z > soma:
                #print("a")
                num = z
                soma = z + divs[l]
                break

    if num != 0:
        print(num)
    else:
        print(n - 1)
