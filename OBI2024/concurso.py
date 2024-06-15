n,k = input().split()

n = int(n)
k = int(k)

a = input().split()

for i in range(0, n):
    a[i] = int(a[i])

a.sort(reverse=True)

corte = a[0]
k -= 1

g = 1
while(True):
    if(k == 0):
        break
    corte = a[g]
    k -= 1
    g += 1

print(corte)
