def est_premier(n):
    """Retourne True si n est un nombre premier."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def liste_premiers(max_val):
    """Retourne une liste de nombres premiers jusqu'à max_val."""
    return [x for x in range(2, max_val + 1) if est_premier(x)]

