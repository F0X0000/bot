import random

def losuj(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        linie = plik.readlines()
        wylosowana_linia = random.choice(linie)
        return wylosowana_linia.strip()
