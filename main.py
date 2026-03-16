from Lecture_fichier import *
from matrice import *
from Floyd_Warshall import *
from pathlib import Path




if __name__ == '__main__':

    dossier = Path("./Graphes/")
    temp = True
    choix_valid = False

    while temp:
        fichiers = [f for f in dossier.iterdir() if f.is_file()]

        if not fichiers:
            print("Aucun fichier dans le répertoire.")
        else:
            print("Liste des fichiers :")
            for i, fichier in enumerate(fichiers, start=1):
                print(f"{i} - {fichier.name}")

            print("0 - Arrêt du programme \n")
            choix = input("Entrez le numéro du fichier à choisir : ")

            if choix.isdigit():
                choix = int(choix)
                if choix == 0:
                    temp = False
                if 1 <= choix <= len(fichiers):
                    fichier_choisi = fichiers[choix - 1]
                    print(f"Vous avez choisi : {fichier_choisi.name} \n")
                    temp = False
                    choix_valid = True

                else:
                    print("Numéro invalide.\n")
            else:
                print("Veuillez entrer un nombre valide.\n")

    if choix_valid:
        lignes = lire_fichier("./Graphes/" + fichier_choisi.name)
        G = creation_matrice(lignes)
        print("Matrice de valeur :")
        print_matrice(G)

        Matrice_adjacente = creation_matrice_adjacente(G)

        print("Execution de l'algorithme de Floyd\n")
        matrice_floyd = algo_floyd(G)
        matrice_floyd_L, matrice_floyd_P= matrice_floyd[0], matrice_floyd[1]

        print("Matrice L :")
        print_matrice(matrice_floyd_L)

        print("\nMatrice P :")
        print_matrice(matrice_floyd_P)

        if detection_circuit_absorbant(matrice_floyd_L):
            print("\nCircuit absorbant detecté dans ce graphe")
        else:
            print("\nAucun circuit absorbent dans le graphe\n")
            cont = True

            recommencer = input("Chemin ? (oui ou non)")
            if recommencer == "oui":
                while cont:
                    sommetA = input("Sommet de départ ?")
                    sommetB = input("Sommet de fin ?")
                    ch_court = chemin_plus_court(matrice_floyd_L,matrice_floyd_P, int(sommetA), int(sommetB))
                    recommencer = input("Recommencer ? (oui ou non)")
                    if recommencer == "non":
                        cont = False
        choix_valid = False