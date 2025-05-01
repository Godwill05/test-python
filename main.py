from api import fetch_joke
from analysis import analyse_joke

def main():
    joke = fetch_joke()
    print("Blague récupérée :")
    print(joke)

    print("\nAnalyse :")
    result = analyse_joke(joke)
    for k, v in result.items():
        print(f"{k} : {v}")

if __name__ == "__main__":
    main()

