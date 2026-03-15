def lire_fichier(fichier):
    with open(fichier, 'r') as f:
        lignes = f.readlines()
    return lignes
