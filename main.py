# main.py
def saluer(nom):
    return f"Bonjour, {nom} !"

if __name__ == "__main__":
    utilisateur = "Alice"
    message = saluer(utilisateur)
    print(message)

