from utils import liste_premiers

def afficher():
    max_val = 50
    premiers = liste_premiers(max_val)
    print(f"Nombres premiers jusqu'à {max_val} :")
    print(premiers)

if __name__ == "__main__":
    afficher()

