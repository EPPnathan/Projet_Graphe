def algo_floyd(matrice_adjacente):
    n = len(matrice_adjacente)
    L = [[999]*n for i in range(n)]
    P = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                L[i][j] = 0
                P[i][j] = i
            elif matrice_adjacente[i][j] is not None:
                L[i][j] = matrice_adjacente[i][j]
                P[i][j] = i
            else:
                L[i][j] = 999
                P[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if L[i][k] + L[k][j] < L[i][j]:
                    L[i][j] = L[i][k] + L[k][j]
                    P[i][j] = P[k][j]
    return [L,P]


def chemin_plus_court(L,P, dep, ar):
    n = len(P)
    i = P[dep][ar]
    temp = 0
    chemin = str(ar)
    while (i != dep) and (temp <= n):
        chemin = str(i) + chemin
        i = P[dep][i]
        temp += 1
    chemin = str(i) + chemin
    print("Le chemin le plus court entre",dep,"et", ar, "est de", L[dep][ar], "saut qui est :", chemin)
    return [chemin,L[dep][ar]]