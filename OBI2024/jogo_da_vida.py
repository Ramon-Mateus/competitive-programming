n,q = input().split()

n = int(n)
q = int(q)

jogo = []
jogoQ1 = []

v = 0

for i in range(0, n):
    row = input()
    jogo.append([])
    for j in range(0, n):
        jogo[i].append(row[j])

def check(i, j, vi):
    if jogo[i][j] == "0":
        if vi == 3:
            jogoQ1[i].append(1)
        else:
            jogoQ1[i].append(0)
    else:
        if(vi == 2 or vi == 3):
            jogoQ1[i].append(1)
        else:
            jogoQ1[i].append(0)

for i in range(0, n):
    jogoQ1.append([])
    for j in range(0, n):
        if i == 0:
            if j == 0:
                if jogo[i][j+1] == "1":
                    v += 1
                if jogo[i+1][j+1] == "1":
                    v += 1
                if jogo[i+1][j] == "1":
                    v += 1
                check(i, j, v)
                v = 0
            elif j == n - 1:
                if jogo[i][j-1] == "1":
                    v += 1
                if jogo[i+1][j-1] == "1":
                    v += 1
                if jogo[i+1][j] == "1":
                    v += 1
                check(i, j, v)
                v = 0
            else:
                if jogo[i][j+1] == "1":
                    v += 1
                if jogo[i+1][j+1] == "1":
                    v += 1
                if jogo[i+1][j] == "1":
                    v += 1
                if jogo[i+1][j-1] == "1":
                    v += 1
                if jogo[i][j-1] == "1":
                    v += 1
                check(i, j, v)
                v = 0
        elif i == n - 1:
            if j == 0:
                if jogo[i-1][j] == "1":
                    v += 1
                if jogo[i-1][j+1] == "1":
                    v += 1
                if jogo[i][j+1] == "1":
                    v += 1
                check(i, j, v)
                v = 0
            elif j == n - 1:
                if jogo[i][j-1] == "1":
                    v += 1
                if jogo[i-1][j-1] == "1":
                    v += 1
                if jogo[i-1][j] == "1":
                    v += 1
                check(i, j, v)
                v = 0
            else:
                if jogo[i][j-1] == "1":
                    v += 1
                if jogo[i-1][j-1] == "1":
                    v += 1
                if jogo[i-1][j] == "1":
                    v += 1
                if jogo[i-1][j+1] == "1":
                    v += 1
                if jogo[i][j+1] == "1":
                    v += 1
                check(i, j, v)
                v = 0
        elif j == 0:
            if jogo[i-1][j] == "1":
                v += 1
            if jogo[i-1][j+1] == "1":
                v += 1
            if jogo[i][j+1] == "1":
                v += 1
            if jogo[i+1][j+1] == "1":
                v += 1
            if jogo[i+1][j] == "1":
                v += 1
            check(i, j, v)
            v = 0
        elif j == n - 1:
            if jogo[i-1][j] == "1":
                v += 1
            if jogo[i-1][j-1] == "1":
                v += 1
            if jogo[i][j-1] == "1":
                v += 1
            if jogo[i+1][j-1] == "1":
                v += 1
            if jogo[i+1][j] == "1":
                v += 1
            check(i, j, v)
            v = 0
        else:
            if jogo[i-1][j-1] == "1":
                v += 1
            if jogo[i-1][j] == "1":
                v += 1
            if jogo[i-1][j+1] == "1":
                v += 1
            if jogo[i][j+1] == "1":
                v += 1
            if jogo[i+1][j+1] == "1":
                v += 1
            if jogo[i+1][j] == "1":
                v += 1
            if jogo[i+1][j-1] == "1":
                v += 1
            if jogo[i][j-1] == "1":
                v += 1
            check(i, j, v)
            v = 0

print("----------------")

for k in range(0, n):
    for w in range(0, n-1):
        print(jogoQ1[k][w], end="")
    print(jogoQ1[k][n-1])