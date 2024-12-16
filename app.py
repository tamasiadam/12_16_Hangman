from country_list import get_countries
import random

countries = get_countries()

#alsóvonalak különválasztása külön szavaknál


print("Üdvözöllek az akasztófa játékban!")
        

def easy():
    life = 7
    jo_tippek = []
    rossz_tippek = []

    orszag_index = random.randint(0, 182)
    orszag = countries[orszag_index]
    orszag_len = len(orszag)
    ismeretlen = orszag_len * "_ "

    print(orszag)
    print(f"A kitalálandó ország: \n{ismeretlen}")
     
    while life > 0:
        
        tipp = input("Adj meg egy betűt, vagy megoldást: ")
        
        if tipp.lower() == orszag.lower():
            print("Gratulálok, nyertél! 🏆")
        
        elif tipp.lower() in orszag.lower():
            jo_tippek.append(tipp)
            print(f"Válaszod helyes, \nRossz válaszok: {rossz_tippek} \nJó válaszok: {jo_tippek}")
            print(ismeretlen)
        
        elif tipp.lower() not in orszag.lower():
            rossz_tippek.append(tipp)
            life -= 1
            print(f"Válaszod helytelen, \nRossz válaszok: {rossz_tippek} \n Jó válaszok: {jo_tippek}")
            print("Megmaradt életed:", life, " 💔")

def kezdes():
    while True:
        jatek_valasztas = int(input("Válassz szintet!\nKönnyű (1)\nKözepes (2)\nNehéz (3)\nVálassz!: "))
        if jatek_valasztas == 1:
            print("Könnyű nehézség kiválasztva! ✅")
            easy()
        elif jatek_valasztas == 2:
            print("Közepes nehézség kiválasztva! ✅")
            medium()
        elif jatek_valasztas == 3:
            print("Nehéz nehézség kiválasztva! ✅")
            hard()
        else:
            print("Helytelen formátum! ❌")

kezdes()