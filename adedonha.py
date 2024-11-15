import random
import string

# Poderia ser algo assim:
# list("abcdefghijklmnopqrstuvwxyz")
alfabeto = string.ascii_letters[:26]

temas = [
    "cidades",
    "paises",
    "comidas",
    "nomes",
    "animais",
    "carros",
    "jogos",
    "empresas"
]

if __name__ == "__main__":
    print(f"Letra: {random.choice(alfabeto)}")
    print(f"Tema: {random.choice(temas)}")
