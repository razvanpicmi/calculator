# Citim valoarea lui N de la utilizator
N = int(input("Introduceți un număr N: "))

# Inițializăm variabila pentru sumă
suma = 0

# Inițializăm un contor
contor = 1

# Bucla while pentru calcularea sumei
while contor <= N:
    suma += contor  # Adăugăm contorul la sumă
    contor += 1  # Incrementăm contorul

# Afișăm rezultatul
print(f"Suma numerelor de la 1 până la {N} este: {suma}")
