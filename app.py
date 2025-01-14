from country_list import get_countries
import random
from ascii import HANGMANPICS
from contry_and_capital_list import countries_and_capitals

countries = get_countries()
capitals = countries_and_capitals()

print("Üdvözöllek az Akasztófa játékban!")

jo_tippek = []
rossz_tippek = []

#Könnyű mód: 7 élet, 1 szavas országok
def easy():
    orszag = random.choice(countries)
    
    while " " in orszag:
        orszag = random.choice(countries)
    
    orszag_len = len(orszag)
    ismeretlen = ""
    
    for i in orszag:
        if i == " ":
            ismeretlen += "   "
        else:
            ismeretlen += "_ "

    elet = 7

    print(orszag)
    print(f"Az ország hossza: {orszag_len} karakter.")
    print(f"A kitalálandó ország: \n{ismeretlen}")

    while elet > 0:
        tipp = input("Adj meg egy betűt, vagy megoldást: ").strip()

        if tipp.lower() == orszag.lower():
            print("Gratulálok, kitaláltad az országot! 🎉")
            while True:
                ask = input("Szeretnél még játszani? (Igen/Nem)")
                if ask.lower() == "igen":
                    jo_tippek.clear()
                    rossz_tippek.clear()
                    kezdes()
                elif ask.lower() == "nem":
                    print("Játék vége!")
                    exit()
                else:
                    print("Ezt nem tudom értelmezni")

        if "_" not in ismeretlen:
            print("Gratulálok, kitaláltad az országot! 🎉")
            
            while True:
                ask = input("Szeretnél még játszani? (Igen/Nem)")
                if ask.lower() == "igen":
                    jo_tippek.clear()
                    rossz_tippek.clear()
                    kezdes()
                elif ask.lower() == "nem":
                    print("Játék vége!")
                    exit()
                else:
                    print("Ezt nem tudom értelmezni")

        #már felhasznált betű
        elif tipp.lower() in jo_tippek or tipp.lower() in rossz_tippek:
            print("Ezt a betűt már próbáltad! ❌")

        #kilépés
        elif tipp.lower() == "quit":
            kilepes = input("- Kilépés -\nBiztos ki akarsz lépni? (igen/nem): ").strip().lower()
            if kilepes == "igen":
                print("Kilépés..")
                exit()
            else:
                print("Játék folytatása...")
                continue

        #helyes betű
        elif tipp.lower() in orszag.lower():
            jo_tippek.append(tipp.lower())
            print(f"Helyes válasz! ✅\n")
            print("Rossz válaszok:", ", ".join(rossz_tippek), "\nJó válaszok:", ", ".join(jo_tippek))

            #megadott betűk kicserélése
            uj_ismeretlen = ""
            for i in range(len(orszag)):
                if orszag[i].lower() == tipp.lower():
                    uj_ismeretlen += orszag[i] + " "
                else:
                    uj_ismeretlen += ismeretlen[i * 2] + " "
            ismeretlen = uj_ismeretlen
            print(ismeretlen)

        #rossz válasz
        elif tipp.lower() not in orszag.lower():
            rossz_tippek.append(tipp.lower())
            elet -= 1
            
            print(HANGMANPICS[6 - elet])
            print(f"Helytelen válasz! ❌>")
            print("> Rossz válaszok:", ", ".join(rossz_tippek), "\n> Jó válaszok:", ", ".join(jo_tippek))
            print("> Megmaradt életed:", elet, " 💔")

            if elet == 0:
                print(f"Vesztettél! Az ország: {orszag}")
                
                while True:
                    ask = input("Szeretnéd újra megpróbálni? (Igen/Nem)")
                    if ask.lower() == "igen":
                        jo_tippek.clear()
                        rossz_tippek.clear()
                        break
                    elif ask.lower() == "nem":
                        print("Játék vége!")
                        exit()
                    else:
                        print("Ezt nem tudom értelmezni! Igen vagy Nem választ fogadok el csak.")

#Közepes mód: 7 élet, többszavas országok
def medium():
    orszag = random.choice(countries)
    orszag_len = len(orszag)
    ismeretlen = ""
    for i in orszag:
        if i == " ":
            ismeretlen += "   "
        else:
            ismeretlen += "_ "

    elet = 7

    print(orszag)
    print(f"Az ország hossza: {orszag_len} karakter.")
    print(f"A kitalálandó ország: \n{ismeretlen}")

    while elet > 0:
        tipp = input("Adj meg egy betűt, vagy megoldást: ").strip()

        #Helyes tipp
        if tipp.lower() == orszag.lower():
            print("Gratulálok, kitaláltad az országot! 🎉")
            
            while True:
                ask = input("Szeretnél még játszani? (Igen/Nem)")
                if ask.lower() == "igen":
                    jo_tippek.clear()
                    rossz_tippek.clear()
                    kezdes()
                elif ask.lower() == "nem":
                    print("Játék vége!")
                    break
                else:
                    print("Ezt nem tudom értelmezni")

        #Nincs több ismeretlen betű
        if "_" not in ismeretlen:
            print("Gratulálok, kitaláltad az országot! 🎉")
            
            while True:
                ask = input("Szeretnél még játszani? (Igen/Nem)")
                if ask.lower() == "igen":
                    jo_tippek.clear()
                    rossz_tippek.clear()
                    kezdes()
                elif ask.lower() == "nem":
                    print("Játék vége!")
                    exit()
                else:
                    print("Ezt nem tudom értelmezni")

        #már felhasznált betű
        elif tipp.lower() in jo_tippek or tipp.lower() in rossz_tippek:
            print("Ezt a betűt már próbáltad! ❌")

        #kilépés
        elif tipp.lower() == "quit":
            kilepes = input("- Kilépés -\nBiztos ki akarsz lépni? (igen/nem): ").strip().lower()
            if kilepes == "igen":
                print("Kilépés..")
                exit()
            else:
                print("Játék folytatása...")
                continue

        #helyes betű
        elif tipp.lower() in orszag.lower():
            jo_tippek.append(tipp.lower())
            print(f"Helyes válasz! ✅>")
            print("> Rossz válaszok:", ", ".join(rossz_tippek), "\n> Jó válaszok:", ", ".join(jo_tippek))

            #megadott betűk kicserélése
            uj_ismeretlen = ""
            for i in range(len(orszag)):
                if orszag[i].lower() == tipp.lower():
                    uj_ismeretlen += orszag[i] + " "
                else:
                    uj_ismeretlen += ismeretlen[i * 2] + " "
            ismeretlen = uj_ismeretlen
            print(ismeretlen)

        #rossz válasz
        elif tipp.lower() not in orszag.lower():
            rossz_tippek.append(tipp.lower())
            elet -= 1
            
            print(HANGMANPICS[6 - elet])
            print(f"Helytelen válasz! ❌")
            print("> Rossz válaszok:", ", ".join(rossz_tippek), "\n> Jó válaszok:", ", ".join(jo_tippek))
            print("> Megmaradt életed:", elet, " 💔")

            if elet == 0:
                print(f"Vesztettél! Az ország: {orszag}")

                while True:
                    ask = input("Szeretnéd újra megpróbálni? (Igen/Nem)")
                    if ask.lower() == "igen":
                        jo_tippek.clear()
                        rossz_tippek.clear()
                        break
                    elif ask.lower() == "nem":
                        print("Játék vége!")
                        exit()
                    else:
                        print("Ezt nem tudom értelmezni! Igen vagy Nem választ fogadok el csak.")

#Nehéz mód: 5 élet, többszavas ország + fővárosa
def hard():
    orszag = random.choice(countries)
    orszag_len = len(orszag)
    fovaros = random.choice(capitals)
    fovaros_len = len(fovaros)
    ismeretlen = ""
    for i in orszag:
        if i == " ":
            ismeretlen += "   "
        elif i == "|":
            ismeretlen += "| "
        else:
            ismeretlen += "_ "

    elet = 5

    print(orszag)
    print(f"Az ország hossza: {orszag_len} karakter.")
    print(f"A kitalálandó ország: \n{ismeretlen}")

    while elet > 0:
        tipp = input("Adj meg egy betűt, vagy megoldást: ").strip()

        if tipp.lower() == orszag.lower():
            print("Gratulálok, kitaláltad az országot! 🎉")
            
            while True:
                ask = input("Szeretnél még játszani? (Igen/Nem)")
                if ask.lower() == "igen":
                    jo_tippek.clear()
                    rossz_tippek.clear()
                    kezdes()
                elif ask.lower() == "nem":
                    print("Játék vége!")
                    exit()
                else:
                    print("Ezt nem tudom értelmezni")
                

        if "_" not in ismeretlen:
            print("Gratulálok, kitaláltad az országot! 🎉")
            while True:
                ask = input("Szeretnél még játszani? (Igen/Nem)")
                if ask.lower() == "igen":
                    jo_tippek.clear()
                    rossz_tippek.clear()
                    kezdes()
                elif ask.lower() == "nem":
                    print("Játék vége!")
                    exit()
                else:
                    print("Ezt nem tudom értelmezni")

        #már felhasznált betű
        elif tipp.lower() in jo_tippek or tipp.lower() in rossz_tippek:
            print("Ezt a betűt már próbáltad! ❌")

        #kilépés
        elif tipp.lower() == "quit":
            kilepes = input("- Kilépés -\nBiztos ki akarsz lépni? (igen/nem): ").strip().lower()
            if kilepes == "igen":
                print("Kilépés..")
                exit()
            else:
                print("Játék folytatása...")
                continue

        #helyes válasz
        elif tipp.lower() in orszag.lower():
            jo_tippek.append(tipp.lower())
            print(f"Helyes válasz! ✅")
            print("> Rossz válaszok:", ", ".join(rossz_tippek), "\n> Jó válaszok:", ", ".join(jo_tippek))

            #megadott betűk kicserélése
            uj_ismeretlen = ""
            for i in range(len(orszag)):
                if orszag[i].lower() == tipp.lower():
                    uj_ismeretlen += orszag[i] + " "
                else:
                    uj_ismeretlen += ismeretlen[i * 2] + " "
            ismeretlen = uj_ismeretlen
            print(ismeretlen)

        #rossz válasz
        elif tipp.lower() not in orszag.lower():
            rossz_tippek.append(tipp.lower())
            elet -= 1
            
            print(HANGMANPICS[6 - elet])
            print(f"Helytelen válasz! ❌")
            print("> Rossz válaszok:", ", ".join(rossz_tippek), "\n> Jó válaszok:", ", ".join(jo_tippek))
            print("> Megmaradt életed:", elet, " 💔")

            if elet == 0:
                print(f"Vesztettél! Az ország: {orszag}")
                while True:
                    ask = input("Szeretnéd újra megpróbálni? (Igen/Nem)")
                    if ask.lower() == "igen":
                        jo_tippek.clear()
                        rossz_tippek.clear()
                        break
                    elif ask.lower() == "nem":
                        print("Játék vége!")
                        exit
                    else:
                        print("Ezt nem tudom értelmezni! Igen vagy Nem választ fogadok el csak.")

#Nehézség kiválasztása
def kezdes():
    while True:
        try:
            jatek_valasztas = int(input("Válassz szintet!\nKönnyű (1)\nKözepes (2)\nNehéz (3)\nVálassz!: "))
            if jatek_valasztas == 1:
                print("Könnyű nehézség kiválasztva! ✅")
                easy()
                break
            elif jatek_valasztas == 2:
                print("Közepes nehézség kiválasztva! ✅")
                medium()
                break
            elif jatek_valasztas == 3:
                print("Nehéz nehézség kiválasztva! ✅")
                hard()
                break
            else:
                print("Helytelen formátum! ❌")
        except ValueError:
            print("Kérlek, számot adj meg! ❌")

kezdes()