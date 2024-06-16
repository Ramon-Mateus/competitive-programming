n,q = input().split()

n = int(n)
q = int(q)

jogoQn = []

v = 0

jogoQn.append([])
for i in range(0, n):
    row = input()
    jogoQn[0].append([])
    for j in range(0, n):
        jogoQn[0][i].append(row[j])

def check(i, j, qi, vi):
    if jogoQn[qi-1][i][j] == "0":
        if vi == 3:
            jogoQn[qi][i].append("1")
        else:
            jogoQn[qi][i].append("0")
    else:
        if(vi == 2 or vi == 3):
            jogoQn[qi][i].append("1")
        else:
            jogoQn[qi][i].append("0")

for k in range(1, q+1):
    jogoQn.append([])
    for i in range(0, n):
        jogoQn[k].append([])
        for j in range(0, n):
            if i == 0:
                if j == 0:
                    if jogoQn[k-1][i][j+1] == "1":
                        v += 1
                    if jogoQn[k-1][i+1][j+1] == "1":
                        v += 1
                    if jogoQn[k-1][i+1][j] == "1":
                        v += 1
                    check(i, j, k, v)
                    v = 0
                elif j == n - 1:
                    if jogoQn[k-1][i][j-1] == "1":
                        v += 1
                    if jogoQn[k-1][i+1][j-1] == "1":
                        v += 1
                    if jogoQn[k-1][i+1][j] == "1":
                        v += 1
                    check(i, j, k, v)
                    v = 0
                else:
                    if jogoQn[k-1][i][j+1] == "1":
                        v += 1
                    if jogoQn[k-1][i+1][j+1] == "1":
                        v += 1
                    if jogoQn[k-1][i+1][j] == "1":
                        v += 1
                    if jogoQn[k-1][i+1][j-1] == "1":
                        v += 1
                    if jogoQn[k-1][i][j-1] == "1":
                        v += 1
                    check(i, j, k, v)
                    v = 0
            elif i == n - 1:
                if j == 0:
                    if jogoQn[k-1][i-1][j] == "1":
                        v += 1
                    if jogoQn[k-1][i-1][j+1] == "1":
                        v += 1
                    if jogoQn[k-1][i][j+1] == "1":
                        v += 1
                    check(i, j, k, v)
                    v = 0
                elif j == n - 1:
                    if jogoQn[k-1][i][j-1] == "1":
                        v += 1
                    if jogoQn[k-1][i-1][j-1] == "1":
                        v += 1
                    if jogoQn[k-1][i-1][j] == "1":
                        v += 1
                    check(i, j, k, v)
                    v = 0
                else:
                    if jogoQn[k-1][i][j-1] == "1":
                        v += 1
                    if jogoQn[k-1][i-1][j-1] == "1":
                        v += 1
                    if jogoQn[k-1][i-1][j] == "1":
                        v += 1
                    if jogoQn[k-1][i-1][j+1] == "1":
                        v += 1
                    if jogoQn[k-1][i][j+1] == "1":
                        v += 1
                    check(i, j, k, v)
                    v = 0
            elif j == 0:
                if jogoQn[k-1][i-1][j] == "1":
                    v += 1
                if jogoQn[k-1][i-1][j+1] == "1":
                    v += 1
                if jogoQn[k-1][i][j+1] == "1":
                    v += 1
                if jogoQn[k-1][i+1][j+1] == "1":
                    v += 1
                if jogoQn[k-1][i+1][j] == "1":
                    v += 1
                check(i, j, k, v)
                v = 0
            elif j == n - 1:
                if jogoQn[k-1][i-1][j] == "1":
                    v += 1
                if jogoQn[k-1][i-1][j-1] == "1":
                    v += 1
                if jogoQn[k-1][i][j-1] == "1":
                    v += 1
                if jogoQn[k-1][i+1][j-1] == "1":
                    v += 1
                if jogoQn[k-1][i+1][j] == "1":
                    v += 1
                check(i, j, k, v)
                v = 0
            else:
                if jogoQn[k-1][i-1][j-1] == "1":
                    v += 1
                if jogoQn[k-1][i-1][j] == "1":
                    v += 1
                if jogoQn[k-1][i-1][j+1] == "1":
                    v += 1
                if jogoQn[k-1][i][j+1] == "1":
                    v += 1
                if jogoQn[k-1][i+1][j+1] == "1":
                    v += 1
                if jogoQn[k-1][i+1][j] == "1":
                    v += 1
                if jogoQn[k-1][i+1][j-1] == "1":
                    v += 1
                if jogoQn[k-1][i][j-1] == "1":
                    v += 1
                check(i, j, k, v)
                v = 0

print("----------------")

for k in range(0, n):
    for w in range(0, n-1):
        print(jogoQn[q][k][w], end="")
    print(jogoQn[q][k][n-1])