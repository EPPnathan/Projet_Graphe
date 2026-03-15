def creation_matrice(lignes):
    nb_sommet = int(lignes[0])
    nb_arc = int(lignes[1])
    matrice_adjacente = [[None]*nb_sommet for j in range(nb_sommet)]
    for i in range(nb_arc):
        a, b, c = lignes[2 + i].split()
        matrice_adjacente[int(a)][int(b)] = int(c)
    return matrice_adjacente

def creation_matrice_adjacente(matrice):
    nb_sommet = len(matrice)
    Mat_AD = [[0]*nb_sommet for j in range(nb_sommet)]
    for i in range(nb_sommet):
        for j in range(nb_sommet):
            if matrice[i][j] is not None:
                Mat_AD[i][j] = 1
    return Mat_AD

def detection_circuit_absorbant(matrice_L):
    for i in range(len(matrice_L)):
        if matrice_L[i][i] < 0:
            return True
    return False

def print_matrice(matrice):
    if not matrice:
        print("Matrice vide")
        return

    nb_lignes = len(matrice)
    nb_colonnes = len(matrice[0])

    # Conversion en texte
    matrice_str = [[str(val) for val in ligne] for ligne in matrice]

    # Largeur automatique
    largeur = max(
        max(len(val) for ligne in matrice_str for val in ligne),
        len(str(nb_lignes - 1)),
        len(str(nb_colonnes - 1))
    ) + 2

    # Ligne séparation matrice uniquement
    def sep_matrice():
        print(" " * (largeur + 1) + "+" + "+".join(["=" * largeur for _ in range(nb_colonnes)]) + "+")

    # Ligne séparation complète
    def sep_complete():
        print("+" + "-" * largeur + "+" + "+".join(["=" * largeur for _ in range(nb_colonnes)]) + "+")

    # En-tête colonnes
    sep_complete()
    print("|" + "Idx".center(largeur) + "|" , end="")
    for j in range(nb_colonnes):
        print(str(j).center(largeur) + "|", end="")
    print()
    sep_complete()

    # Lignes
    for i in range(nb_lignes):
        print("|" + str(i).center(largeur) + "|", end="")
        for val in matrice_str[i]:
            print(val.center(largeur) + "|", end="")
        print()
        sep_matrice()