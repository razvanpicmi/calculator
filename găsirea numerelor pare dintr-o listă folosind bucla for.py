# Lista de numere
lista = [10, 15, 20, 25, 30, 35]

# Listă pentru stocarea numerelor pare
numere_pare = []

# Parcurgem lista folosind o buclă for
for numar in lista:
    if numar % 2 == 0:  # Verificăm dacă numărul este par
        numere_pare.append(numar)  # Adăugăm numărul la lista de numere pare

# Afișăm rezultatul
print(f"Numerele pare din listă sunt: {numere_pare}")
