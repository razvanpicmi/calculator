# Lista originală
lista = [1, 2, 3, 4, 5]

# Creăm o listă inversată
lista_inversata = []

# Parcurgem lista de la ultimul element spre primul
for i in range(len(lista) - 1, -1, -1):
    lista_inversata.append(lista[i])  # Adăugăm elementul la lista inversată

# Afișăm lista inversată
print(f"Lista inversată este: {lista_inversata}")
