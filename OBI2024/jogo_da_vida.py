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

for i in range(0, n):
    jogoQ1.append([])
    for j in range(0, n):
        if i == 0:
            if j == 0:
                if jogo[i,j+1] == 1:
                    v += 1
                if jogo[i+1,j+1] == 1:
                    v += 1
                if jogo[i+1,j] == 1:
                    v += 1
                if jogo[i][j] == 0:
                    if v == 3:
                        jogoQ1[i][j] = 1
                    else:
                        jogoQ1[i][j] = 0
                else:
                    if(v == 2 or v == 3):
                        jogoQ1[i][j] = 1
                    else:
                        jogoQ1[i][j] = 0
            elif j == n - 1:
                if jogo[i,j-1] == 1:
                    v += 1
                if jogo[i-1,j-1] == 1:
                    v += 1
                if jogo[i-1,j] == 1:
                    v += 1
                if jogo[i][j] == 0:
                    if v == 3:
                        jogoQ1[i][j] = 1
                    else:
                        jogoQ1[i][j] = 0
                else:
                    if(v == 2 or v == 3):
                        jogoQ1[i][j] = 1
                    else:
                        jogoQ1[i][j] = 0
            else:
                if jogo[i,j+1] == 1:
                    v += 1
                if jogo[i+1,j+1] == 1:
                    v += 1
                if jogo[i+1,j] == 1:
                    v += 1
                if jogo[i,j-1] == 1:
                    v += 1
                if jogo[i-1,j-1] == 1:
                    v += 1
                if jogo[i][j] == 0:
                    if v == 3:
                        jogoQ1[i][j] = 1
                    else:
                        jogoQ1[i][j] = 0
                else:
                    if(v == 2 or v == 3):
                        jogoQ1[i][j] = 1
                    else:
                        jogoQ1[i][j] = 0
