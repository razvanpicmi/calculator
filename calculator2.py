# Funcție pentru a solicita un număr de la utilizator
def citeste_numar(prompt):
    while True:
        try:
            # Solicităm utilizatorului să introducă un număr
            return float(input(prompt))
        except ValueError:
            # Gestionăm eroarea în caz că utilizatorul introduce un șir invalid
            print("Valoare invalidă. Vă rugăm să introduceți un număr valid.")

# Citim cele două numere de la utilizator
numar1 = citeste_numar("Introduceți primul număr: ")
numar2 = citeste_numar("Introduceți al doilea număr: ")

# Calculăm suma celor două numere
suma = numar1 + numar2

# Afișăm rezultatul
print(f"Suma celor două numere este: {suma}")
