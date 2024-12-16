from country_list import get_countries
import random

countries = get_countries()

print("Üdvözöllek az Akasztófa játékban!")

orszag_index = random.randint(0, 182) #182 vagy 183?
orszag = countries[orszag_index]
orszag_len = len(orszag)
ismeretlen = ""
for i in orszag:
    if i == " ":
        ismeretlen += "   "
    else:
        ismeretlen += "_ "
jo_tippek = []
rossz_tippek = []


def easy():
    life = 7

    print(f"Az ország: {orszag}")
    print(f"Hossz: {orszag_len}")
    print(f"A kitalálandó ország: \n{ismeretlen}")

    while life > 0:
        
        tipp = input("Adj meg egy betűt, vagy megoldást: ")
        
        if tipp.lower() == orszag.lower():
            print("Gratulálok, nyertél! 🏆")
        
        elif tipp.lower() in jo_tippek or rossz_tippek: #kis- és nagybetűk különbözőnek számítanak, ezt egyenlőként kéne kezelni
            print("Ezt a betűt már próbáltad! ❌")
        
        elif tipp.lower() in orszag.lower():
            jo_tippek.append(tipp)
            print(f"Helyes válasz! ✅\nRossz válaszok: {rossz_tippek} \nJó válaszok: {jo_tippek}")
            #replace?
            #megkeresni hol vannak azok a betűk, ott kicserélni pontosan, ha van többet is akár
            print(ismeretlen)
        
        elif tipp.lower() not in orszag.lower():
            rossz_tippek.append(tipp)
            life -= 1
            print(f"Helytelen válasz! ❌\n>Rossz válaszok: {rossz_tippek}\n>Jó válaszok: {jo_tippek}")
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
        
        else:
            print("Helytelen formátum! ❌")

kezdes()