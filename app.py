from country_list import get_countries
import random

countries = get_countries()

print("Üdvözöllek az akasztófa játékban!")
        

def easy():
    orszagok = random.randint(countries)
    print(orszagok)
    
def kezdes():

    while True:
        jatek_valasztas = int(input("Válassz szintet!\nKönnyű (1)\nKözepes (2)\nNehéz (3)\nVálassz!: "))
        if jatek_valasztas == 1:
            print("Könnyű nehézség kiválasztva! ✅")
            easy()
        if jatek_valasztas == 2:
            print("Közepes nehézség kiválasztva! ✅")
            medium()
        if jatek_valasztas == 3:
            print("Nehéz nehézség kiválasztva! ✅")
            hard()
        else:
            print("Helytelen formátum! ❌")

kezdes()