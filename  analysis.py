def analyse_joke(joke: str) -> dict:
    return {
        "longueur": len(joke),
        "mots": len(joke.split()),
        "commence_par_chuck": joke.lower().startswith("chuck")
    }

