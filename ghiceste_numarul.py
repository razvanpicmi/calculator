import random

# Generăm un număr aleatoriu între 1 și 100
numar_secret = random.randint(1, 100)

# Inițializăm o variabilă pentru a stoca încercările utilizatorului
incercare = None

print("Am ales un număr între 1 și 100. Încearcă să-l ghicești!")

# Bucla while se repetă până când utilizatorul ghicește numărul
while incercare != numar_secret:
    # Citim încercarea utilizatorului
    incercare = int(input("Introduceți un număr: "))

    # Verificăm dacă numărul este prea mic
    if incercare < numar_secret:
        print("Prea mic! Mai încearcă.")
    # Verificăm dacă numărul este prea mare
    elif incercare > numar_secret:
        print("Prea mare! Mai încearcă.")
    # Dacă numărul este corect
    else:
        print(f"Felicitări! Ai ghicit numărul {numar_secret}.")
