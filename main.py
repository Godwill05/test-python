def calculer_moyenne_ponderee(matieres):
    total_points = 0
    total_coefficients = 0
    for matiere in matieres:
        note = matiere["note"]
        coeff = matiere["coefficient"]
        total_points += note * coeff
        total_coefficients += coeff
    return total_points / total_coefficients

def afficher_resultats(matieres, moyenne):
    print("Résultats des matières :")
    print("{:<15} {:<10} {:<12}".format("Matière", "Note", "Coefficient"))
    for m in matieres:
        print("{:<15} {:<10} {:<12}".format(m["nom"], m["note"], m["coefficient"]))
    print(f"\nMoyenne générale : {moyenne:.2f}")
    print("Décision :", "Admis" if moyenne >= 10 else "Ajourné")

def main():
    matieres = [
        {"nom": "Mathématiques", "note": 14, "coefficient": 4},
        {"nom": "Physique", "note": 12, "coefficient": 3},
        {"nom": "Chimie", "note": 10, "coefficient": 2},
        {"nom": "Biologie", "note": 11, "coefficient": 2},
        {"nom": "Histoire", "note": 9, "coefficient": 1},
        {"nom": "Géographie", "note": 13, "coefficient": 1},
        {"nom": "Informatique", "note": 15, "coefficient": 3}
    ]
    moyenne = calculer_moyenne_ponderee(matieres)
    afficher_resultats(matieres, moyenne)

if __name__ == "__main__":
    main()
