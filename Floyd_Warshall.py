def algo_floyd(matrice_adjacente):
    n = len(matrice_adjacente)
    L = [[float('inf')]*n for i in range(n)]
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
                L[i][j] = float('inf')
                P[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if L[i][k] + L[k][j] < L[i][j]:
                    L[i][j] = L[i][k] + L[k][j]
                    P[i][j] = P[k][j]
    return [L,P]


def chemin_plus_court(L, P, dep, ar):
    n = len(P)
    if L[dep][ar] == float('inf'):
        print(f"Pas de chemin entre {dep} et {ar}")
        return [None, float('inf')]

    chemin = []
    current = ar

    while current != -1:
        chemin.append(current)
        if current == dep:
            break
        current = P[dep][current]

    chemin.reverse()
    chemin_str = " → ".join(map(str, chemin))
    distance = L[dep][ar]

    if distance == float('inf'):
        distance_str = "∞"
    else:
        distance_str = str(distance)

    print(f"Le chemin le plus court entre {dep} et {ar} est de longueur {distance_str} : {chemin_str}")
    return [chemin_str, distance]